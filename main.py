# Importando arquivos de execução do programa
from src.processing.extraction import extraction
from src.processing.cleaning import cleaning
from src.processing.analisys import analisys
from src.graphics.bar_charts import plot_bar_charts
from src.graphics.box_plot import plot_box_plot
from src.graphics.distribution_graph import plot_distribution_graph
from src.graphics.histograms import plot_histograms
from src.graphics.line_charts import plot_line_charts
from src.graphics.pie_charts import plot_pie_charts
from src.graphics.radar_charts import plot_radar_charts
from src.graphics.scatter_plots import plot_scatter_plots
from src.models.gumbel import gumbel
from src.models.linear_regression import linear_regression
from src.models.logistic_regression import logistic_regression
from src.predictions import predicting
from app import app, set_param

def main():
    # Realiza a extração dos dados
    print("Realizando a limpeza de dados, o processo pode demorar um pouco...")
    extraction()

    # Realiza a limpeza dos dados
    print("Realizando a limpeza dos dados...")
    cleaning()

    # Realiza a análise dos dados
    print("Realizando o análise dos dados...")
    search_result = analisys()
    set_param(search_result)

    # Realiza a criação dos gráficos
    print("Realizando a criação dos gráficos...")
    plot_scatter_plots()
    plot_radar_charts()
    plot_pie_charts()
    plot_line_charts()
    plot_histograms()
    plot_distribution_graph()
    plot_box_plot()
    plot_bar_charts()

    # Realiza a execução dos modelos
    print("Executando o modelo Gumbel...")
    gumbel()
    print("Executando a regressão linear...")
    linear_regression()
    print("Executando a regressão logística...")
    logistic_regression()

    # Realiza as previsões
    print("Fazendo previsões...")
    home_or_away = int(input("Onde será o jogo (Casa 0, Fora 1)? "))
    while home_or_away != 0 and home_or_away != 1:
        home_or_away = int(input("Onde será o jogo (Casa 0, Fora 1)? "))
    predicting(home_or_away)

# Executa o programa
if __name__ == "__main__":
    main()
    app.run(debug=False)
