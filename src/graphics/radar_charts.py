# Importando bibliotecas
import pandas as pd
import plotly.express as px

# Função para plotar gráficos de radar
def plot_radar_charts():
    # Importando os dados
    miami_heat_23_24_games_table = pd.read_csv('data/exported/miami_heat_games_table_23_24.csv')
    miami_heat_24_25_games_table = pd.read_csv('data/exported/miami_heat_games_table_24_25.csv')

    # Criando as colunas de vitórias e derrotas das temporadas
    miami_heat_23_24_games_table['Season'] = '2023-24'
    miami_heat_24_25_games_table['Season'] = '2024-25'

    # Concatenando os dados
    miami_heat_both_seasons_games_table = pd.concat([miami_heat_23_24_games_table, miami_heat_24_25_games_table], ignore_index=True)

    # Criando as colunas de pontos marcados e sofridos
    miami_heat_both_seasons_games_table[['Team_Points', 'Opponent_Points']] = miami_heat_both_seasons_games_table['Score'].str.split(' - ', expand=True).astype(int)
    miami_heat_both_seasons_games_table = miami_heat_both_seasons_games_table.rename(columns={'Home or Road': 'Casa ou Fora'})

    # Criando os dados para o gráfico radar
    radar_data = (
        miami_heat_both_seasons_games_table.groupby(['Season', 'Casa ou Fora'])
        .agg({
            'Team_Points': 'mean', 
            'Opponent_Points': 'mean'
            })
        .reset_index()
        .rename(columns={
            'Team_Points': 'Pontos marcados', 
            'Opponent_Points': 'Pontos sofridos'
            })
    )

    # Dados combinados
    combined_data = (
        miami_heat_both_seasons_games_table.groupby('Casa ou Fora')
        .agg({
            'Team_Points': 'mean', 
            'Opponent_Points': 'mean'
            })
        .reset_index()
        .rename(columns={
            'Team_Points': 'Pontos marcados', 
            'Opponent_Points': 'Pontos sofridos'
            })
    )

    # Adicionando a temporada
    combined_data['Season'] = 'Combined'

    # Concatenando os dados
    radar_data = pd.concat([radar_data, combined_data], ignore_index=True)

    # Adicionando deslocamento para evitar sobreposição
    radar_data['Pontos marcados'] += 0.5
    radar_data['Pontos sofridos'] -= 0.5

    # Função para criar o gráfico radar
    def create_radar_chart(data, season):
        # Filtrando os dados
        season_data = data[data['Season'] == season]
        
        # Plotando o gráfico
        fig = px.line_polar(
            season_data.melt(
                id_vars=['Casa ou Fora'], 
                value_vars=['Pontos marcados', 'Pontos sofridos']
                ),
            r='value',
            theta='variable',
            color='Casa ou Fora',
            line_close=True,
            title=f'Gráfico radar - {season}',
        )
        return fig
    
    # Criando os gráficos
    radar_23_24 = create_radar_chart(radar_data, '2023-24')
    radar_24_25 = create_radar_chart(radar_data, '2024-25')
    radar_combined = create_radar_chart(radar_data, 'Combined')

    # Salvando os gráficos
    radar_23_24.write_image('static/images/radar/miami_heat_points_scored_23_24.png')
    radar_24_25.write_image('static/images/radar/miami_heat_points_scored_24_25.png')
    radar_combined.write_image('static/images/radar/miami_heat_points_scored_combined.png')