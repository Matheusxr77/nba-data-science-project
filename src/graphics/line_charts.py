# Importando bibliotecas
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Função para plotar gráficos de linha
def plot_line_charts():
    # Importando os dados
    miami_heat_23_24_summary = pd.read_csv('data/processed/miami_heat_games_23_24.csv')
    miami_heat_24_25_summary = pd.read_csv('data/processed/miami_heat_games_24_25.csv')

    # Concatenando os dados
    miami_heat_both_seasons_summary = pd.concat([miami_heat_23_24_summary, miami_heat_24_25_summary], ignore_index=True)

    # Criando a coluna de resultado
    miami_heat_both_seasons_summary['Resultado'] = miami_heat_both_seasons_summary['WL'].apply(lambda x: 'Vitória' if x == 'W' else 'Derrota')

    # Convertendo a coluna de data
    miami_heat_both_seasons_summary['GAME_DATE'] = pd.to_datetime(miami_heat_both_seasons_summary['GAME_DATE'])

    # Criando a coluna de Ano-Mês
    miami_heat_both_seasons_summary['Ano-Mês'] = miami_heat_both_seasons_summary['GAME_DATE'].dt.to_period('M')

    # Agrupando os dados
    resultados_por_mês = miami_heat_both_seasons_summary.groupby(['Ano-Mês', 'Resultado']).size().unstack(fill_value=0).reset_index()

    # Convertendo a coluna de Ano-Mês
    resultados_por_mês['Ano-Mês'] = resultados_por_mês['Ano-Mês'].dt.strftime('%b-%Y')

    # Derretendo os dados
    resultados_por_mês = resultados_por_mês.melt(
        id_vars=['Ano-Mês'], 
        value_vars=['Vitória', 'Derrota'], 
        var_name='Resultado', 
        value_name='Quantidade')

    # Plotando o gráfico
    fig = px.line(
        resultados_por_mês, 
        x='Ano-Mês', 
        y='Quantidade', 
        color='Resultado',
        title='Vitórias e Derrotas do Miami Heat por mês (Temporadas 23/24 e 24/25)',
        labels={
            'Ano-Mês': 'Mês', 
            'Quantidade': 'Quantidade'
            },
        color_discrete_map={
            'Vitória': 'green', 
            'Derrota': 'red'
            }
        )
    
    # Atualizando o layout
    fig.update_layout(xaxis=dict(type='category'))

    # Salvando o gráfico
    fig.write_image('static/images/line/resultados_por_mês.png')