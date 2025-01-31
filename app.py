# Importando bibliotecas
from flask import Flask, render_template
import pandas as pd

# Define a variável global search_term
search_term = 'NBA'

# Define a variável app
app = Flask(__name__)

# Define a função set_param
def set_param(value):
    global search_term
    search_term = value

# Define a rota principal
@app.route('/')
def index():
    # Tabelas de conferências
    west_conference = pd.read_csv('data/processed/west_conference.csv')
    east_conference = pd.read_csv('data/processed/east_conference.csv')

    # Tabelas de resumo do Miami Heat
    miami_heat_summary_23_24 = pd.read_csv('data/exported/miami_heat_23_24_summary.csv')
    miami_heat_summary_24_25 = pd.read_csv('data/exported/miami_heat_24_25_summary.csv')

    # Tabelas de resumo do Miami Heat divididas em partes
    miami_heat_summary_23_24_pt1 = pd.read_csv('data/exported/miami_heat_summary_23_24_pt1.csv')
    miami_heat_summary_24_25_pt1 = pd.read_csv('data/exported/miami_heat_summary_24_25_pt1.csv')
    miami_heat_summary_23_24_pt2 = pd.read_csv('data/exported/miami_heat_summary_23_24_pt2.csv')
    miami_heat_summary_24_25_pt2 = pd.read_csv('data/exported/miami_heat_summary_24_25_pt2.csv')

    # Tabelas de resumo defensivo do Miami Heat
    miami_heat_defensive_summary_23_24 = pd.read_csv('data/exported/miami_heat_defensive_summary_23_24.csv')
    miami_heat_defensive_summary_24_25 = pd.read_csv('data/exported/miami_heat_defensive_summary_24_25.csv')

    # Tabelas de jogos dos jogadores do Miami Heat
    bam_adebayo_profile = pd.read_csv('data/processed/bam_adebayo_profile.csv')
    tyler_herro_profile = pd.read_csv('data/processed/tyler_herro_profile.csv')
    jimmy_butler_profile = pd.read_csv('data/processed/jimmy_butler_profile.csv')

    # Tabelas de jogos dos jogadores do Miami Heat na temporada 24-25
    bam_adebayo_games_table_24_25 = pd.read_csv('data/exported/bam_adebayo_games_table_24_25.csv')
    tyler_herro_games_table_24_25 = pd.read_csv('data/exported/tyler_herro_games_table_24_25.csv')
    jimmy_butler_games_table_24_25 = pd.read_csv('data/exported/jimmy_butler_games_table_24_25.csv')

    # Tabelas de jogos dos jogadores do Miami Heat contra o time X
    bam_adebayo_games_against_x = pd.read_csv(f'data/exported/bam_adebayo_games_against_{search_term}.csv')
    tyler_herro_games_against_x = pd.read_csv(f'data/exported/tyler_herro_games_against_{search_term}.csv')
    jimmy_butler_games_against_x = pd.read_csv(f'data/exported/jimmy_butler_games_against_{search_term}.csv')

    # Tabelas de jogos dos jogadores do Miami Heat contra o Orlando Magic
    bam_adebayo_vs_magic = pd.read_csv('data/exported/bam_adebayo_games_vs_magic.csv')
    tyler_herro_vs_magic = pd.read_csv('data/exported/tyler_herro_games_vs_magic.csv')
    jimmy_butler_vs_magic = pd.read_csv('data/exported/jimmy_butler_games_vs_magic.csv')

    # Tabelas de estatísticas dos jogadores do Miami Heat
    bam_adebayo_stats_23_24 = pd.read_csv('data/exported/bam_adebayo_23_24_stats.csv')
    bam_adebayo_stats_24_25 = pd.read_csv('data/exported/bam_adebayo_24_25_stats.csv')
    tyler_herro_stats_23_24 = pd.read_csv('data/exported/tyler_herro_23-24_stats.csv')
    tyler_herro_stats_24_25 = pd.read_csv('data/exported/tyler_herro_24-25_stats.csv')
    jimmy_butler_stats_23_24 = pd.read_csv('data/exported/jimmy_butler_23-24_stats.csv')
    jimmy_butler_stats_24_25 = pd.read_csv('data/exported/jimmy_butler_24-25_stats.csv')

    # Tabelas de estatísticas da carreira dos jogadores do Miami Heat
    bam_adebayo_stats_career = pd.read_csv('data/exported/bam_adebayo_combined_stats.csv')
    tyler_herro_stats_career = pd.read_csv('data/exported/tyler_herro_combined_stats.csv')
    jimmy_butler_stats_career = pd.read_csv('data/exported/jimmy_butler_combined_stats.csv')

    # Tabelas de distribuição dos jogadores do Miami Heat
    tyler_herro_predictions = pd.read_csv('data/exported/tyler_herro_predictions.csv')
    jimmy_butler_predictions = pd.read_csv('data/exported/jimmy_butler_predictions.csv')
    bam_adebayo_predictions = pd.read_csv('data/exported/bam_adebayo_predictions.csv')

    # Renderiza o template index.html
    return render_template(
        # Define o template a ser renderizado
        'index.html',

        # Cria as variáveis que serão utilizadas no template (Equipe)
        east_conference=east_conference.to_html(classes='table table-striped', index=True),
        west_conference=west_conference.to_html(classes='table table-striped', index=True),

        # Define as tabelas que serão utilizadas no template
        miami_heat_summary_23_24=miami_heat_summary_23_24.to_html(classes='table table-striped', index=False),
        miami_heat_summary_24_25=miami_heat_summary_24_25.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template divididas em partes
        miami_heat_summary_23_24_pt1=miami_heat_summary_23_24_pt1.to_html(classes='table table-striped', index=False),
        miami_heat_summary_24_25_pt1=miami_heat_summary_24_25_pt1.to_html(classes='table table-striped', index=False),
        miami_heat_summary_23_24_pt2=miami_heat_summary_23_24_pt2.to_html(classes='table table-striped', index=False),
        miami_heat_summary_24_25_pt2=miami_heat_summary_24_25_pt2.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template (Defesa)
        miami_heat_defensive_summary_23_24=miami_heat_defensive_summary_23_24.to_html(classes='table table-striped', index=False),
        miami_heat_defensive_summary_24_25=miami_heat_defensive_summary_24_25.to_html(classes='table table-striped', index=False),

        # Define as imagens que serão utilizadas de gráfico de barras
        bar_wins_losses_23_24='images/bar/miami_heat_wins_losses_23_24.png',
        bar_wins_losses_24_25='images/bar/miami_heat_wins_losses_24_25.png',

        # Define as imagens que serão utilizadas de gráfico de histograma
        histogram_wins_losses='images/histogram/resultados_por_mês.png',

        # Define as imagens que serão utilizadas de gráfico de pizza
        pie_home_away_win_losses_23_24 = 'images/pie/miami_heat_home_away_wins_losses_23_24.png',
        pie_home_away_win_losses_24_25 = 'images/pie/miami_heat_home_away_wins_losses_24_25.png',

        # Define as imagens que serão utilizadas de gráfico de linha
        line_wins_losses = 'images/line/resultados_por_mês.png',

        # Define as imagens que serão utilizadas de gráfico de dispersão
        scatter_points_23_24 = 'images/scatter/miami_heat_points_23_24.png',
        scatter_points_24_25 = 'images/scatter/miami_heat_points_24_25.png',

        # Define variáveis que serão utilizadas no template (Jogadores)
        bam_adebayo_profile=bam_adebayo_profile.to_html(classes='table table-striped', index=False),
        tyler_herro_profile=tyler_herro_profile.to_html(classes='table table-striped', index=False),
        jimmy_butler_profile=jimmy_butler_profile.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template
        bam_adebayo_games_table_24_25=bam_adebayo_games_table_24_25.to_html(classes='table table-striped', index=False),
        tyler_herro_games_table_24_25=tyler_herro_games_table_24_25.to_html(classes='table table-striped', index=False),
        jimmy_butler_games_table_24_25=jimmy_butler_games_table_24_25.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template (jogadores vs. jogadores)
        bam_adebayo_games_against_x=bam_adebayo_games_against_x.to_html(classes='table table-striped', index=False),
        tyler_herro_games_against_x=tyler_herro_games_against_x.to_html(classes='table table-striped', index=False),
        jimmy_butler_games_against_x=jimmy_butler_games_against_x.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template (jogadores vs. Orlando Magic)
        bam_adebayo_vs_magic=bam_adebayo_vs_magic.to_html(classes='table table-striped', index=False),
        tyler_herro_vs_magic=tyler_herro_vs_magic.to_html(classes='table table-striped', index=False),
        jimmy_butler_vs_magic=jimmy_butler_vs_magic.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template (Estatísticas)
        bam_adebayo_stats_23_24=bam_adebayo_stats_23_24.to_html(classes='table table-striped', index=False),
        bam_adebayo_stats_24_25=bam_adebayo_stats_24_25.to_html(classes='table table-striped', index=False),
        tyler_herro_stats_23_24=tyler_herro_stats_23_24.to_html(classes='table table-striped', index=False),
        tyler_herro_stats_24_25=tyler_herro_stats_24_25.to_html(classes='table table-striped', index=False),
        jimmy_butler_stats_23_24=jimmy_butler_stats_23_24.to_html(classes='table table-striped', index=False),
        jimmy_butler_stats_24_25=jimmy_butler_stats_24_25.to_html(classes='table table-striped', index=False),

        # Define as tabelas que serão utilizadas no template (Estatísticas da carreira)
        bam_adebayo_stats_career=bam_adebayo_stats_career.to_html(classes='table table-striped', index=False),
        tyler_herro_stats_career=tyler_herro_stats_career.to_html(classes='table table-striped', index=False),
        jimmy_butler_stats_career=jimmy_butler_stats_career.to_html(classes='table table-striped', index=False),

        # Define as imagens que serão utilizadas de gráfico de distribuição
        distribution_bam_adebayo_ast = 'images/distribution/bam_adebayo_AST_distribution.png',
        distribution_bam_adebayo_pts = 'images/distribution/bam_adebayo_PTS_distribution.png',
        distribution_bam_adebayo_reb = 'images/distribution/bam_adebayo_REB_distribution.png',
        distribution_jimmy_butler_ast = 'images/distribution/jimmy_butler_AST_distribution.png',
        distribution_jimmy_butler_pts = 'images/distribution/jimmy_butler_PTS_distribution.png',
        distribution_jimmy_butler_reb = 'images/distribution/jimmy_butler_REB_distribution.png',
        distribution_tyler_herro_ast = 'images/distribution/tyler_herro_AST_distribution.png',
        distribution_tyler_herro_pts = 'images/distribution/tyler_herro_PTS_distribution.png',
        distribution_tyler_herro_reb = 'images/distribution/tyler_herro_REB_distribution.png',

        # Define as imagens que serão utilizadas de gráfico de box plot
        box_plot = 'images/box_plot/box_plot.png',

        # Define as imagens que serão utilizadas de gráfico de linha
        line_bam_adebayo_assists_probabilities='images/line/bam_adebayo_assists_probabilities.png',
        line_bam_adebayo_points_probabilities='images/line/bam_adebayo_points_probabilities.png',
        line_bam_adebayo_rebounds_probabilities='images/line/bam_adebayo_rebounds_probabilities.png',
        line_jimmy_butler_assists_probabilities='images/line/jimmy_butler_assists_probabilities.png',
        line_jimmy_butler_points_probabilities='images/line/jimmy_butler_points_probabilities.png',
        line_jimmy_butler_rebounds_probabilities='images/line/jimmy_butler_rebounds_probabilities.png',
        line_tyler_herro_assists_probabilities='images/line/tyler_herro_assists_probabilities.png',
        line_tyler_herro_points_probabilities='images/line/tyler_herro_points_probabilities.png',
        line_tyler_herro_rebounds_probabilities='images/line/tyler_herro_rebounds_probabilities.png',

        # Define as imagens que serão utilizadas de gráfico de barras
        bar_bam_adebayo_ast_probabilities='images/bar/bam_adebayo_ast_probabilities.png',
        bar_bam_adebayo_pts_probabilities='images/bar/bam_adebayo_pts_probabilities.png',
        bar_bam_adebayo_reb_probabilities='images/bar/bam_adebayo_reb_probabilities.png',
        bar_jimmy_butler_ast_probabilities='images/bar/jimmy_butler_ast_probabilities.png',
        bar_jimmy_butler_pts_probabilities='images/bar/jimmy_butler_pts_probabilities.png',
        bar_jimmy_butler_reb_probabilities='images/bar/jimmy_butler_reb_probabilities.png',
        bar_tyler_herro_ast_probabilities='images/bar/tyler_herro_ast_probabilities.png',
        bar_tyler_herro_pts_probabilities='images/bar/tyler_herro_pts_probabilities.png',
        bar_tyler_herro_reb_probabilities='images/bar/tyler_herro_reb_probabilities.png',

        # Define as imagens que serão utilizadas da curva ROC
        bam_adebayo_roc_curve='images/roc/bam_adebayo_games_table_all_seasons_roc_curve.png',
        jimmy_butler_roc_curve='images/roc/jimmy_butler_games_table_all_seasons_roc_curve.png',
        tyler_herro_roc_curve='images/roc/tyler_herro_games_table_all_seasons_roc_curve.png',

        # Define as imagens que serão utilizadas das previsões
        chart_bam_adebayo_predictions='images/predictions/bam_adebayo_predictions.png',
        chart_jimmy_butler_predictions='images/predictions/jimmy_butler_predictions.png',
        chart_tyler_herro_predictions='images/predictions/tyler_herro_predictions.png',

        # Define as tabelas que serão utilizadas das previsões
        bam_adebayo_predictions=bam_adebayo_predictions.to_html(classes='table table-striped', index=False),
        tyler_herro_predictions=tyler_herro_predictions.to_html(classes='table table-striped', index=False),
        jimmy_butler_predictions=jimmy_butler_predictions.to_html(classes='table table-striped', index=False)
    )
