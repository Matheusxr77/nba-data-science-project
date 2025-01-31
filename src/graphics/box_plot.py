# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# Função para plotar gráficos de box plot
def plot_box_plot():
    # Importando os dados
    bam_adebayo_games = pd.read_csv('data/exported/bam_adebayo_games_table_24_25.csv')
    tyler_herro_games = pd.read_csv('data/exported/tyler_herro_games_table_24_25.csv')
    jimmy_butler_games = pd.read_csv('data/exported/jimmy_butler_games_table_24_25.csv')

    # Concatenando os dados
    games = pd.concat([
        bam_adebayo_games.assign(Player='bam_adebayo'),
        tyler_herro_games.assign(Player='tyler_herro'),
        jimmy_butler_games.assign(Player='jimmy_butler')
        ])
    
    # Derretendo os dados
    games_melted = games.melt(
        id_vars=['Player'],
        value_vars=['PTS', 'REB', 'AST'],
        var_name='Statistic', 
        value_name='Value'
        )
    
    # Plotando o gráfico
    fig = px.box(
        games_melted, 
        x='Statistic', 
        y='Value', 
        color='Player',
        points='all', title='Gráfico Box Plot para pontos, assistencias e rebotes por jogo',
        labels={
            'Value': 'Value', 
            'Statistic': 'Statistic'
            }
        )
    
    # Salvando o gráfico
    pio.write_image(fig, 'static/images/box_plot/box_plot.png')