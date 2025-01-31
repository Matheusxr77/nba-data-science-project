# Importando bibliotecas
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Função para plotar gráficos de distribuição
def plot_distribution_graph():
    # Importando os dados
    bam_adebayo_games = pd.read_csv('data/exported/bam_adebayo_games_table_24_25.csv')
    tyler_herro_games = pd.read_csv('data/exported/tyler_herro_games_table_24_25.csv')
    jimmy_butler_games = pd.read_csv('data/exported/jimmy_butler_games_table_24_25.csv')

    # Função para plotar gráficos de distribuição
    def distribution_graph(data, player_name, stat):
        # Verificando se a coluna existe
        if stat in data.columns:
            fig = px.histogram(data, x=stat, nbins=20, title=f'{player_name} - {stat} Distribution')
            fig.add_vline(x=data[stat].mean(), line_dash="dash", line_color="red", annotation_text="Mean")
            fig.add_vline(x=data[stat].median(), line_dash="dash", line_color="green", annotation_text="Median")
            fig.add_vline(x=data[stat].mode()[0], line_dash="dash", line_color="blue", annotation_text="Mode")
            pio.write_image(fig, f'static/images/distribution/{player_name}_{stat}_distribution.png')
        else:
            print(f"Coluna '{stat}' não existe para os dados do jogador {player_name}.")

    # Estatísticas
    stats = ['PTS', 'AST', 'REB']

    # Jogadores
    players = {
        'bam_adebayo': bam_adebayo_games,
        'tyler_herro': tyler_herro_games,
        'jimmy_butler': jimmy_butler_games
    }

    # Plotando os gráficos
    for player, data in players.items():
        for stat in stats:
            distribution_graph(data, player, stat)