# Importando bibliotecas
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from pygam import PoissonGAM, s
from scipy.stats import poisson
from plotly.subplots import make_subplots

# Função para fazer previsões
def predicting(home_or_away):
    # Carregar dados
    bam_adebayo = pd.read_csv('data/exported/bam_adebayo_games_table_all_seasons.csv')
    tyler_herro = pd.read_csv('data/exported/tyler_herro_games_table_all_seasons.csv')
    jimmy_butler = pd.read_csv('data/exported/jimmy_butler_games_table_all_seasons.csv')
    bam_adebayo_stats = pd.read_csv('data/exported/bam_adebayo_all_seasons_stats.csv')
    tyler_herro_stats = pd.read_csv('data/exported/tyler_herro_all_seasons_stats.csv')
    jimmy_butler_stats = pd.read_csv('data/exported/jimmy_butler_all_seasons_stats.csv')

    # Mapear 'Home or Road' para 0 e 1
    bam_adebayo['Home or Road'] = bam_adebayo['Home or Road'].map({'Home': 0, 'Road': 1})
    tyler_herro['Home or Road'] = tyler_herro['Home or Road'].map({'Home': 0, 'Road': 1})
    jimmy_butler['Home or Road'] = jimmy_butler['Home or Road'].map({'Home': 0, 'Road': 1})

    # Função para treinar e prever
    def train_and_predict(player_data, home_away):
        # Selecionar features e alvos
        features = ['Home or Road', 'MIN', 'FGA']

        # Divisão em treino e teste
        X = player_data[features]
        y_points = player_data['PTS']
        y_rebounds = player_data['REB']
        y_assists = player_data['AST']

        # Divisão em treino e teste
        X_train, X_test, y_train_points, y_test_points = train_test_split(X, y_points, test_size=0.2, random_state=42)
        _, _, y_train_rebounds, y_test_rebounds = train_test_split(X, y_rebounds, test_size=0.2, random_state=42)
        _, _, y_train_assists, y_test_assists = train_test_split(X, y_assists, test_size=0.2, random_state=42)

        # Treinamento dos modelos
        gam_points = PoissonGAM(s(0) + s(1) + s(2)).fit(X_train, y_train_points)
        gam_rebounds = PoissonGAM(s(0) + s(1) + s(2)).fit(X_train, y_train_rebounds)
        gam_assists = PoissonGAM(s(0) + s(1) + s(2)).fit(X_train, y_train_assists)

        # Previsões para o próximo jogo
        X_value = [[home_away, player_data['MIN'].mean(), player_data['FGA'].mean()]]
        mu_points = gam_points.predict_mu(X_value)
        mu_rebounds = gam_rebounds.predict_mu(X_value)
        mu_assists = gam_assists.predict_mu(X_value)

        # Definir thresholds como a média dos pontos, rebotes e assistências
        threshold_points = y_points.mean()
        threshold_rebounds = y_rebounds.mean()
        threshold_assists = y_assists.mean()

        # Probabilidades de valores extremos
        prob_above_threshold_points = 1 - poisson.cdf(threshold_points, mu_points)
        prob_below_threshold_points = poisson.cdf(threshold_points, mu_points)
        prob_above_threshold_rebounds = 1 - poisson.cdf(threshold_rebounds, mu_rebounds)
        prob_below_threshold_rebounds = poisson.cdf(threshold_rebounds, mu_rebounds)
        prob_above_threshold_assists = 1 - poisson.cdf(threshold_assists, mu_assists)
        prob_below_threshold_assists = poisson.cdf(threshold_assists, mu_assists)

        return {
            'points': (mu_points, prob_above_threshold_points, prob_below_threshold_points),
            'rebounds': (mu_rebounds, prob_above_threshold_rebounds, prob_below_threshold_rebounds),
            'assists': (mu_assists, prob_above_threshold_assists, prob_below_threshold_assists)
        }, gam_points, gam_rebounds, gam_assists
    
    # Função para visualizar os resultados
    def visualize(gam_points, gam_rebounds, gam_assists, X, y_points, y_rebounds, y_assists, output_png='visualizations.png'):
        # Configurar gráficos interativos com plotly
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=[
                "Points: Coefficients", "Points: Predictions vs Actual",
                "Rebounds: Coefficients", "Rebounds: Predictions vs Actual",
                "Assists: Coefficients", "Assists: Predictions vs Actual"
            ]
        )

        # Títulos e modelos
        titles = ['Points', 'Rebounds', 'Assists']
        models = [gam_points, gam_rebounds, gam_assists]
        y_values = [y_points, y_rebounds, y_assists]

        # Adicionar gráficos
        for i, (model, y, title) in enumerate(zip(models, y_values, titles)):
            # Linha do gráfico
            row = i + 1

            # Gráfico de Coeficientes
            fig.add_trace(
                go.Scatter(
                    y=model.coef_, 
                    mode='lines+markers', 
                    name=f'{title}: Coefficients'
                    ),
                row=row, col=1
            )

            # Gerar X_pred com o mesmo número de features
            X_pred = np.tile(X.mean(axis=0), (100, 1))  # Média dos valores em X para preencher
            X_pred[:, 1] = np.linspace(X['MIN'].min(), X['MIN'].max(), 100)  # Variar minutos jogados

            # Previsões
            y_pred = model.predict(X_pred)
            
            # Gráfico de Previsões vs Atual
            fig.add_trace(
                go.Scatter(
                    x=X_pred[:, 1], 
                    y=y_pred, 
                    mode='lines', 
                    name=f'{title}: Predicted'
                    ),
                row=row, col=2
            )

            fig.add_trace(
                go.Scatter(
                    x=X['MIN'], 
                    y=y, 
                    mode='markers', 
                    name=f'{title}: Actual', 
                    marker=dict(color='red')
                    ),
                row=row, col=2
            )

        # Atualizar layout
        fig.update_layout(
            height=900, width=1200,
            title_text="Visualizations",
            showlegend=False
        )

        # Salvar em arquivo PNG
        fig.write_image(output_png)

    # Fazer previsões para os jogadores
    predictions, gam_points, gam_rebounds, gam_assists = train_and_predict(bam_adebayo, home_or_away)

    # Criar DataFrame com as previsões
    predictions_df = pd.DataFrame({
        'Player': ['bam_adebayo'],
        'Points Predicted': [predictions['points'][0][0]],
        'Average_Points': [bam_adebayo_stats['Average Points'].mean()],
        'Prob_Points_Above_Average': [predictions['points'][1][0]],
        'Prob_Points_Below_Average': [predictions['points'][2][0]],
        'Assists Predicted': [predictions['assists'][0][0]],
        'Average_Assists': [bam_adebayo_stats['Average Assists'].mean()],
        'Prob_Assists_Above_Average': [predictions['assists'][1][0]],
        'Prob_Assists_Below_Average': [predictions['assists'][2][0]],
        'Rebounds Predicted': [predictions['rebounds'][0][0]],
        'Average_Rebounds': [bam_adebayo_stats['Average Rebounds'].mean()],
        'Prob_Rebounds_Above_Average': [predictions['rebounds'][1][0]],
        'Prob_Rebounds_Below_Average': [predictions['rebounds'][2][0]]
    })

    # Salvar DataFrame em um arquivo CSV
    predictions_df.to_csv('data/exported/bam_adebayo_predictions.csv', index=False)

    # Bam Adebayo
    X_bam_adebayo = bam_adebayo[['Home or Road', 'MIN', 'FGA']]
    y_bam_adebayo_points = bam_adebayo['PTS']
    y_bam_adebayo_rebounds = bam_adebayo['REB']
    y_bam_adebayo_assists = bam_adebayo['AST']

    # Visualizar previsões
    visualize(
        gam_points, 
        gam_rebounds, 
        gam_assists, 
        X_bam_adebayo, 
        y_bam_adebayo_points, 
        y_bam_adebayo_rebounds, 
        y_bam_adebayo_assists, 
        'static/images/predictions/bam_adebayo_predictions.png'
    )

    # Tyler Herro
    predictions_tyler_herro, gam_points_tyler_herro, gam_rebounds_tyler_herro, gam_assists_tyler_herro = train_and_predict(tyler_herro, home_or_away)
    
    # Criar DataFrame com as previsões de Tyler Herro
    predictions_tyler_herro_df = pd.DataFrame({
        'Player': ['tyler_herro'],
        'Points Predicted': [predictions_tyler_herro['points'][0][0]],
        'Average_Points': [tyler_herro_stats['Average Points'].mean()],
        'Prob_Points_Above_Average': [predictions_tyler_herro['points'][1][0]],
        'Prob_Points_Below_Average': [predictions_tyler_herro['points'][2][0]],
        'Assists Predicted': [predictions_tyler_herro['assists'][0][0]],
        'Average_Assists': [tyler_herro_stats['Average Assists'].mean()],
        'Prob_Assists_Above_Average': [predictions_tyler_herro['assists'][1][0]],
        'Prob_Assists_Below_Average': [predictions_tyler_herro['assists'][2][0]],
        'Rebounds Predicted': [predictions_tyler_herro['rebounds'][0][0]],
        'Average_Rebounds': [tyler_herro_stats['Average Rebounds'].mean()],
        'Prob_Rebounds_Above_Average': [predictions_tyler_herro['rebounds'][1][0]],
        'Prob_Rebounds_Below_Average': [predictions_tyler_herro['rebounds'][2][0]]
    })

    # Salvar DataFrame em um arquivo CSV
    predictions_tyler_herro_df.to_csv('data/exported/tyler_herro_predictions.csv', index=False)

    # Tyler Herro
    X_tyler_herro = tyler_herro[['Home or Road', 'MIN', 'FGA']]
    y_tyler_herro_points = tyler_herro['PTS']
    y_tyler_herro_rebounds = tyler_herro['REB']
    y_tyler_herro_assists = tyler_herro['AST']

    # Visualizar previsões
    visualize(
        gam_points_tyler_herro, 
        gam_rebounds_tyler_herro, 
        gam_assists_tyler_herro, 
        X_tyler_herro, 
        y_tyler_herro_points, 
        y_tyler_herro_rebounds, 
        y_tyler_herro_assists, 
        'static/images/predictions/tyler_herro_predictions.png'
    )

    # Jimmy Butler
    predictions_jimmy_butler, gam_points_jimmy_butler, gam_rebounds_jimmy_butler, gam_assists_jimmy_butler = train_and_predict(jimmy_butler, home_or_away)
    
    # Criar DataFrame com as previsões de Jimmy Butler
    predictions_jimmy_butler_df = pd.DataFrame({
        'Player': ['jimmy_butler'],
        'Points Predicted': [predictions_jimmy_butler['points'][0][0]],
        'Average_Points': [jimmy_butler_stats['Average Points'].mean()],
        'Prob_Points_Above_Average': [predictions_jimmy_butler['points'][1][0]],
        'Prob_Points_Below_Average': [predictions_jimmy_butler['points'][2][0]],
        'Assists Predicted': [predictions_jimmy_butler['assists'][0][0]],
        'Average_Assists': [jimmy_butler_stats['Average Assists'].mean()],
        'Prob_Assists_Above_Average': [predictions_jimmy_butler['assists'][1][0]],
        'Prob_Assists_Below_Average': [predictions_jimmy_butler['assists'][2][0]],
        'Rebounds Predicted': [predictions_jimmy_butler['rebounds'][0][0]],
        'Average_Rebounds': [jimmy_butler_stats['Average Rebounds'].mean()],
        'Prob_Rebounds_Above_Average': [predictions_jimmy_butler['rebounds'][1][0]],
        'Prob_Rebounds_Below_Average': [predictions_jimmy_butler['rebounds'][2][0]]
    })

    # Salvar DataFrame em um arquivo CSV
    predictions_jimmy_butler_df.to_csv('data/exported/jimmy_butler_predictions.csv', index=False)

    # Jimmy Butler
    X_jimmy_butler = jimmy_butler[['Home or Road', 'MIN', 'FGA']]
    y_jimmy_butler_points = jimmy_butler['PTS']
    y_jimmy_butler_rebounds = jimmy_butler['REB']
    y_jimmy_butler_assists = jimmy_butler['AST']

    # Visualizar previsões
    visualize(
        gam_points_jimmy_butler, 
        gam_rebounds_jimmy_butler, 
        gam_assists_jimmy_butler, 
        X_jimmy_butler, 
        y_jimmy_butler_points, 
        y_jimmy_butler_rebounds, 
        y_jimmy_butler_assists, 
        'static/images/predictions/jimmy_butler_predictions.png'
    )