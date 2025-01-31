# Importando bibliotecas
import pandas as pd
import plotly.graph_objects as go
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import StandardScaler

# Função para ajustar a regressão logística
def logistic_regression():
    # Função para processar os dados do jogador
    def process_player(file_path):
        # Importando os dados
        data = pd.read_csv(file_path)

        # Selecionando as colunas
        X = data[['MIN', 'FGA', 'TOV']]
        y = data['PTS']

        # Normalizando os dados
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Dividindo os dados
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Ajustando o modelo
        y_train = (y_train > y_train.median()).astype(int)
        y_test = (y_test > y_test.median()).astype(int)

        # Treinando o modelo
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # Calculando as probabilidades
        y_pred_proba = model.predict_proba(X_test)

        # Calculando a área sob a curva ROC
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)

        # Plotando a curva ROC
        fig_roc = go.Figure()

        # Adicionando as curvas
        fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC curve (area = {roc_auc:.2f})'))
        fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', line=dict(dash='dash'), name='F(x) = x'))

        # Atualizando o layout
        fig_roc.update_layout(
            title='Receiver Operating Characteristic', 
            xaxis_title='False Positive Rate', 
            yaxis_title='True Positive Rate'
            )
        
        # Salvando a imagem
        os.makedirs('static/images/roc', exist_ok=True)
        fig_roc.write_image(f"static/images/roc/{file_path.split('/')[-1].split('.')[0]}_roc_curve.png")

    # Arquivos dos jogadores
    player_files = [
        'data/exported/bam_adebayo_games_table_all_seasons.csv',
        'data/exported/tyler_herro_games_table_all_seasons.csv',
        'data/exported/jimmy_butler_games_table_all_seasons.csv'
    ]

    # Processando os jogadores
    for file in player_files:
        process_player(file)