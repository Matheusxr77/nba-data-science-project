# Importando bibliotecas
import pandas as pd
import plotly.express as px

# Função para plotar histogramas
def plot_histograms():
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

    # Plotando o gráfico
    fig = px.bar(
        resultados_por_mês, 
        x='Ano-Mês', 
        y=['Vitória', 'Derrota'],
        title='Vitórias e Derrotas do Detroit miami_heat por mês (Temporadas 23/24 e 24/25)',
        labels={'Ano-Mês': 'Mês', 'value': 'Quantidade'},
        color_discrete_map={
            'Vitória': 'green',
            'Derrota': 'red'
            }
        )
    
    # Atualizando o layout
    fig.update_layout(xaxis=dict(type='category'), barmode='group')

    # Salvando o gráfico
    fig.write_image('static/images/histogram/resultados_por_mês.png')