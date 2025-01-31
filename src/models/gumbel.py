# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.stats import gumbel_r

# Função para ajustar a distribuição de Gumbel
def gumbel():
    # Importando os dados
    bam_adebayo = pd.read_csv('data/exported/bam_adebayo_games_table_all_seasons.csv')
    tyler_herro = pd.read_csv('data/exported/tyler_herro_games_table_all_seasons.csv')
    jimmy_butler = pd.read_csv('data/exported/jimmy_butler_games_table_all_seasons.csv')

    # Função para distribuição de Gumbel
    def fit_gumbel(data):
        params = gumbel_r.fit(data)
        return params
    
    # Função para calcular a probabilidade de x
    def probability_above_x(params, x):
        return 1 - gumbel_r.cdf(x, *params)
    
    # Função para calcular a probabilidade de pelo menos x
    def probability_at_least_x(params, x):
        return 1 - gumbel_r.cdf(x, *params)
    
    # Função para calcular a probabilidade de no máximo x
    def probability_at_most_x(params, x):
        return gumbel_r.cdf(x, *params)
    
    # Função para calcular a proporção de valores menores ou iguais a x
    def proportion_below_or_equal_x(data, x):
        return np.mean(data <= x)
    
    # Função para calcular a proporção de valores abaixo de x
    def values_below_x(data, x):
        return data[data < x]
    
    # Função para plotar as probabilidades e proporções
    def proportion_below_x(data, x):
        return np.mean(data < x)
    
    # Cálculos para Bam Adebayo
    bam_adebayo_points = bam_adebayo['PTS']
    bam_adebayo_rebounds = bam_adebayo['REB']
    bam_adebayo_assists = bam_adebayo['AST']

    # Parâmetros para os pontos de Bam Adebayo
    bam_adebayo_points_params = fit_gumbel(bam_adebayo_points)
    bam_adebayo_rebounds_params = fit_gumbel(bam_adebayo_rebounds)
    bam_adebayo_assists_params = fit_gumbel(bam_adebayo_assists)

    # Cálculos para Tyler Herro
    tyler_herro_points = tyler_herro['PTS']
    tyler_herro_rebounds = tyler_herro['REB']
    tyler_herro_assists = tyler_herro['AST']

    # Parâmetros para os pontos de Tyler Herro
    tyler_herro_points_params = fit_gumbel(tyler_herro_points)
    tyler_herro_rebounds_params = fit_gumbel(tyler_herro_rebounds)
    tyler_herro_assists_params = fit_gumbel(tyler_herro_assists)

    # Cálculos para Jimmy Butler
    jimmy_butler_points = jimmy_butler['PTS']
    jimmy_butler_rebounds = jimmy_butler['REB']
    jimmy_butler_assists = jimmy_butler['AST']

    # Parâmetros para os pontos de Jimmy Butler
    jimmy_butler_points_params = fit_gumbel(jimmy_butler_points)
    jimmy_butler_rebounds_params = fit_gumbel(jimmy_butler_rebounds)
    jimmy_butler_assists_params = fit_gumbel(jimmy_butler_assists)

    # Função para plotar as probabilidades e proporções
    def plot_probabilities_and_proportions(data, params, title, x_label, file_name):
        # Valores de x
        x_values = np.linspace(min(data), max(data), 100)

        # Cálculos
        prob_above = [probability_above_x(params, x) for x in x_values]
        prob_at_least = [probability_at_least_x(params, x) for x in x_values]
        prob_at_most = [probability_at_most_x(params, x) for x in x_values]
        prop_below_or_equal = [proportion_below_or_equal_x(data, x) for x in x_values]
        prop_below = [proportion_below_x(data, x) for x in x_values]

        # Plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_values, y=prob_above, mode='lines', name='Probabilidade de mais que x'))
        fig.add_trace(go.Scatter(x=x_values, y=prob_at_least, mode='lines', name='Probabilidade de pelo menos x'))
        fig.add_trace(go.Scatter(x=x_values, y=prob_at_most, mode='lines', name='Probabilidade de no máximo x'))
        fig.add_trace(go.Scatter(x=x_values, y=prop_below_or_equal, mode='lines', name='Proporção de valores menores ou iguais a x'))
        fig.add_trace(go.Scatter(x=x_values, y=prop_below, mode='lines', name='Proporção de valores abaixo de x'))

        # Layout
        fig.update_layout(
            title=title,
            xaxis_title=x_label,
            yaxis_title='Probabilidade/Proporção',
            legend_title='Legenda',
            template='plotly_white'
        )

        # Salvar o gráfico
        fig.write_image(file_name)

    # Bam Adebayo
    plot_probabilities_and_proportions(bam_adebayo_points, bam_adebayo_points_params, 'Probabilidades e Proporções para Pontos de bam_adebayo', 'Pontos', 'static/images/line/bam_adebayo_points_probabilities.png')
    plot_probabilities_and_proportions(bam_adebayo_rebounds, bam_adebayo_rebounds_params, 'Probabilidades e Proporções para Rebotes de bam_adebayo', 'Rebotes', 'static/images/line/bam_adebayo_rebounds_probabilities.png')
    plot_probabilities_and_proportions(bam_adebayo_assists, bam_adebayo_assists_params, 'Probabilidades e Proporções para Assistências de bam_adebayo', 'Assistências', 'static/images/line/bam_adebayo_assists_probabilities.png')

    # Tyler Herro
    plot_probabilities_and_proportions(tyler_herro_points, tyler_herro_points_params, 'Probabilidades e Proporções para Pontos de tyler_herro', 'Pontos', 'static/images/line/tyler_herro_points_probabilities.png')
    plot_probabilities_and_proportions(tyler_herro_rebounds, tyler_herro_rebounds_params, 'Probabilidades e Proporções para Rebotes de tyler_herro', 'Rebotes', 'static/images/line/tyler_herro_rebounds_probabilities.png')
    plot_probabilities_and_proportions(tyler_herro_assists, tyler_herro_assists_params, 'Probabilidades e Proporções para Assistências de tyler_herro', 'Assistências', 'static/images/line/tyler_herro_assists_probabilities.png')

    # Jimmy Butler
    plot_probabilities_and_proportions(jimmy_butler_points, jimmy_butler_points_params, 'Probabilidades e Proporções para Pontos de jimmy_butler', 'Pontos', 'static/images/line/jimmy_butler_points_probabilities.png')
    plot_probabilities_and_proportions(jimmy_butler_rebounds, jimmy_butler_rebounds_params, 'Probabilidades e Proporções para Rebotes de jimmy_butler', 'Rebotes', 'static/images/line/jimmy_butler_rebounds_probabilities.png')
    plot_probabilities_and_proportions(jimmy_butler_assists, jimmy_butler_assists_params, 'Probabilidades e Proporções para Assistências de jimmy_butler', 'Assistências', 'static/images/line/jimmy_butler_assists_probabilities.png')