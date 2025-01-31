# Importar bibliotecas
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Função para ajustar a regressão linear
def linear_regression():
    # Importando os dados
    bam_adebayo = pd.read_csv('data/exported/bam_adebayo_games_table_all_seasons.csv')
    tyler_herro = pd.read_csv('data/exported/tyler_herro_games_table_all_seasons.csv')
    jimmy_butler = pd.read_csv('data/exported/jimmy_butler_games_table_all_seasons.csv')

    # Função para dividir os dados
    def split_data(player_data, target):
        X = player_data[['MIN', 'FGA', 'TOV']]
        y = player_data[target]
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Função para treinar o modelo
    def train_model(X_train, y_train):
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    # Função para calcular as probabilidades
    def calculate_probabilities(predictions, actual):
        mean = np.mean(actual)
        median = np.median(actual)
        mode = actual.mode()[0]
        maximum = np.max(actual)
        minimum = np.min(actual)

        # Probabilidades
        probabilities = {
            'above_mean': np.mean(predictions > mean),
            'below_mean': np.mean(predictions < mean),
            'above_median': np.mean(predictions > median),
            'below_median': np.mean(predictions < median),
            'above_mode': np.mean(predictions > mode),
            'below_mode': np.mean(predictions < mode),
            'above_maximum': np.mean(predictions > maximum),
            'below_maximum': np.mean(predictions < maximum),
            'above_minimum': np.mean(predictions > minimum),
            'below_minimum': np.mean(predictions < minimum)
        }

        return probabilities
    
    # Função para plotar as probabilidades
    def plot_probabilities(probabilities, title, filename):
        categories = list(probabilities.keys())
        values = list(probabilities.values())

        fig = go.Figure(data=[go.Bar(name='Probability', x=categories, y=values)])

        fig.update_layout(
            title=title,
            xaxis_title='Category',
            yaxis_title='Probability',
            barmode='group'
        )

        fig.write_image(filename)

    # Função para processar os dados dos jogadores
    def process_player_data(player_data, player_name):
        targets = ['PTS', 'AST', 'REB']

        # Processar os dados para cada alvo
        for target in targets:
            X_train, X_test, y_train, y_test = split_data(player_data, target)
            model = train_model(X_train, y_train)
            predictions = model.predict(X_test)
            probabilities = calculate_probabilities(predictions, y_test)
            plot_probabilities(probabilities, f'{player_name} {target} Probabilities', f'static/images/bar/{player_name}_{target.lower()}_probabilities.png')

    # Processar dados de todos os jogadores
    process_player_data(bam_adebayo, 'bam_adebayo')
    process_player_data(tyler_herro, 'tyler_herro')
    process_player_data(jimmy_butler, 'jimmy_butler')