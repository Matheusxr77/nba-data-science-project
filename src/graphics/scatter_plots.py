# Importando bibliotecas
import pandas as pd
import plotly.express as px

# Função para plotar gráficos de análise
def plot_scatter_plots():
    # Importando os dados
    miami_heat_game_table_23_24 = pd.read_csv('data/exported/miami_heat_games_table_23_24.csv')
    miami_heat_game_table_24_25 = pd.read_csv('data/exported/miami_heat_games_table_24_25.csv')

    # Criando as colunas de vitórias e derrotas das temporadas
    miami_heat_game_table_23_24['Season'] = '2023-24'
    miami_heat_game_table_24_25['Season'] = '2024-25'

    # Concatenando os dados
    miami_heat_game_table_both_seasons = pd.concat([miami_heat_game_table_23_24, miami_heat_game_table_24_25], ignore_index=True)

    # Criando as colunas de pontos marcados e sofridos
    miami_heat_game_table_both_seasons['Points_Marked'], miami_heat_game_table_both_seasons['Points_Conceded'] = zip(
        *miami_heat_game_table_both_seasons['Score'].str.split(' - ').apply(lambda x: (int(x[0]), int(x[1])))
    )

    # Resumo dos dados
    miami_heat_summary = miami_heat_game_table_both_seasons.groupby(['Season', 'Adversary']).agg({
        'Points_Marked': 'mean',
        'Points_Conceded': 'mean'
    }).reset_index()

    # Resumo combinado
    miami_heat_summary_combined = miami_heat_summary.groupby('Adversary').agg({
        'Points_Marked': 'mean',
        'Points_Conceded': 'mean'
    }).reset_index()

    # Plotando os gráficos
    graph_23_24 = px.scatter(
        miami_heat_summary[miami_heat_summary['Season'] == '2023-24'],
        x='Points_Conceded',
        y='Points_Marked',
        text='Adversary',
        title='Pontos Marcados vs. Sofridos - Temporada 2023-24',
        labels={
            'Points_Conceded': 'Pontos Sofridos (Média)', 
            'Points_Marked': 'Pontos Marcados (Média)'
            },
        color_discrete_sequence=['blue']
    )

    # Atualizando a posição do texto
    graph_23_24.update_traces(textposition='top center')
    
    graph_24_25 = px.scatter(
        miami_heat_summary[miami_heat_summary['Season'] == '2024-25'],
        x='Points_Conceded',
        y='Points_Marked',
        text='Adversary',
        title='Pontos Marcados vs. Sofridos - Temporada 2024-25',
        labels={
            'Points_Conceded': 'Pontos Sofridos (Média)', 
            'Points_Marked': 'Pontos Marcados (Média)'
            },
        color_discrete_sequence=['green']
    )

    # Atualizando a posição do texto
    graph_24_25.update_traces(textposition='top center')

    combined_graph = px.scatter(
        miami_heat_summary_combined,
        x='Points_Conceded',
        y='Points_Marked',
        text='Adversary',
        title='Pontos Marcados vs. Sofridos - Média das Temporadas 2023-24 e 2024-25',
        labels={
            'Points_Conceded': 'Pontos Sofridos (Média)', 
            'Points_Marked': 'Pontos Marcados (Média)'
            },
        color_discrete_sequence=['purple']
    )

    # Atualizando a posição do texto
    combined_graph.update_traces(textposition='top center')

    # Salvando os gráficos
    graph_23_24.write_image('static/images/scatter/miami_heat_points_23_24.png')
    graph_24_25.write_image('static/images/scatter/miami_heat_points_24_25.png')
    combined_graph.write_image('static/images/scatter/miami_heat_points_combined.png')