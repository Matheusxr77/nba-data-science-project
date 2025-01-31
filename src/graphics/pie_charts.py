# Importando bibliotecas
import pandas as pd
import plotly.express as px

# Função para plotar gráficos de pizza
def plot_pie_charts():
    # Importando os dados
    miami_heat_23_24_summary = pd.read_csv('data/exported/miami_heat_23_24_summary.csv')
    miami_heat_24_25_summary = pd.read_csv('data/exported/miami_heat_24_25_summary.csv')

    # Criando as colunas de vitórias e derrotas das temporadas
    miami_heat_23_24_summary['Season'] = '2023-24'
    miami_heat_24_25_summary['Season'] = '2024-25'

    # Concatenando os dados
    miami_heat_both_seasons_summary = pd.concat([miami_heat_23_24_summary, miami_heat_24_25_summary], ignore_index=True)

    # Criando as colunas de vitórias e derrotas
    miami_heat_both_seasons_summary['Vitórias'] = miami_heat_both_seasons_summary['Total Wins']
    miami_heat_both_seasons_summary['Vitórias em casa'] = miami_heat_both_seasons_summary['Home Wins']
    miami_heat_both_seasons_summary['Vitórias fora de casa'] = miami_heat_both_seasons_summary['Road Wins']
    miami_heat_both_seasons_summary['Derrotas'] = miami_heat_both_seasons_summary['Total Losses']
    miami_heat_both_seasons_summary['Derrotas em casa'] = miami_heat_both_seasons_summary['Home Losses']
    miami_heat_both_seasons_summary['Derrotas fora de casa'] = miami_heat_both_seasons_summary['Road Losses']

    # Criando o gráfico de vitórias e derrotas
    miami_heat_home_away_win_losses_all = miami_heat_both_seasons_summary.melt(
        id_vars=['Season'], 
        value_vars=[
            'Vitórias em casa', 
            'Vitórias fora de casa', 
            'Derrotas em casa', 
            'Derrotas fora de casa'
            ], 
        var_name='Resultado', 
        value_name='Quantidade'
        )
    
    # Agrupando as vitórias e derrotas
    miami_heat_home_away_all_data = miami_heat_home_away_win_losses_all.groupby(['Resultado']).sum(numeric_only=True).reset_index()

    # Criando a ordem das categorias
    category_order = [
        'Vitórias em casa', 
        'Vitórias fora de casa', 
        'Derrotas em casa', 
        'Derrotas fora de casa'
        ]
    
    # Plotando o gráfico
    miami_heat_home_away_all_data_graph = px.pie(
        miami_heat_home_away_all_data, 
        names='Resultado', 
        values='Quantidade', 
        color='Resultado',
        color_discrete_map={
            'Vitórias em casa': 'green', 
            'Vitórias fora de casa': 'blue', 
            'Derrotas em casa':'red', 
            'Derrotas fora de casa': 'brown'
            },
        title='Vitórias e derrotas do Miami Heat nas temporadas 23-24 e 24-25',
        category_orders={'Resultado': category_order}
        )
    
    # Filtrando os dados
    miami_heat_home_away_23_24_data = miami_heat_home_away_win_losses_all[miami_heat_home_away_win_losses_all['Season'] == '2023-24']
    miami_heat_home_away_24_25_data = miami_heat_home_away_win_losses_all[miami_heat_home_away_win_losses_all['Season'] == '2024-25']

    # Agrupando os dados
    miami_heat_home_away_23_24_data_grouped = miami_heat_home_away_23_24_data.groupby(['Resultado']).sum(numeric_only=True).reset_index()
    miami_heat_home_away_24_25_data_grouped = miami_heat_home_away_24_25_data.groupby(['Resultado']).sum(numeric_only=True).reset_index()

    # Plotando os gráficos
    miami_heat_home_away_23_24_graph = px.pie(
        miami_heat_home_away_23_24_data_grouped, 
        names='Resultado', 
        values='Quantidade', 
        color='Resultado',
        color_discrete_map={
            'Vitórias em casa': 'green', 
            'Vitórias fora de casa': 'blue', 
            'Derrotas em casa':'red', 
            'Derrotas fora de casa': 'brown'
            },
        title='Vitórias e derrotas do Miami Heat na temporada 23-24',
        category_orders={'Resultado': category_order}
        )

    miami_heat_home_away_24_25_graph = px.pie(
        miami_heat_home_away_24_25_data_grouped, 
        names='Resultado', 
        values='Quantidade', 
        color='Resultado',
        color_discrete_map={
            'Vitórias em casa': 'green', 
            'Vitórias fora de casa': 'blue', 
            'Derrotas em casa':'red', 
            'Derrotas fora de casa': 'brown'
            },
        title='Vitórias e derrotas do Miami Heat na temporada 24-25',
        category_orders={'Resultado': category_order}
        )
    
    # Salvando os gráficos
    miami_heat_home_away_all_data_graph.write_image('static/images/pie/miami_heat_home_away_wins_losses_all.png')
    miami_heat_home_away_23_24_graph.write_image('static/images/pie/miami_heat_home_away_wins_losses_23_24.png')
    miami_heat_home_away_24_25_graph.write_image('static/images/pie/miami_heat_home_away_wins_losses_24_25.png')