# Importando biblioteca
import pandas as pd

# Função para análise dos dados
def analisys():
    # Importando arquivos com os dados dos jogadores e times
    bam_adebayo_23_24 = pd.read_csv('data/processed/bam_adebayo_stats_23_24.csv')
    bam_adebayo_24_25 = pd.read_csv('data/processed/bam_adebayo_stats_24_25.csv')
    tyler_herro_23_24 = pd.read_csv('data/processed/tyler_herro_stats_23_24.csv')
    tyler_herro_24_25 = pd.read_csv('data/processed/tyler_herro_stats_24_25.csv')
    jimmy_butler_23_24 = pd.read_csv('data/processed/jimmy_butler_stats_23_24.csv')
    jimmy_butler_24_25 = pd.read_csv('data/processed/jimmy_butler_stats_24_25.csv')
    miami_heat_23_24 = pd.read_csv('data/processed/miami_heat_games_23_24.csv')
    miami_heat_24_25 = pd.read_csv('data/processed/miami_heat_games_24_25.csv')
    miami_heat_21_22 = pd.read_csv('data/processed/miami_heat_games_21_22.csv')
    miami_heat_22_23 = pd.read_csv('data/processed/miami_heat_games_22_23.csv')
    bam_adebayo_all_seasons = pd.read_csv('data/processed/bam_adebayo_all_seasons_games.csv')
    tyler_herro_all_seasons = pd.read_csv('data/processed/tyler_herro_all_seasons_games.csv')
    jimmy_butler_all_seasons = pd.read_csv('data/processed/jimmy_butler_all_seasons_games.csv')

    # Concatenando dados de todas as temporadas
    miami_heat_all_seasons = pd.concat([
        miami_heat_21_22, 
        miami_heat_22_23, 
        miami_heat_23_24, 
        miami_heat_24_25
    ], ignore_index=True)

    # Filtrar jogos em casa e fora
    home_games_24_25 = miami_heat_24_25[miami_heat_24_25['MATCHUP'].str.contains('@') == False]
    road_games_24_25 = miami_heat_24_25[miami_heat_24_25['MATCHUP'].str.contains('@')]
    home_games_23_24 = miami_heat_23_24[miami_heat_23_24['MATCHUP'].str.contains('@') == False]
    road_games_23_24 = miami_heat_23_24[miami_heat_23_24['MATCHUP'].str.contains('@')]

    # Contar vitórias
    total_wins_24_25 = miami_heat_24_25[miami_heat_24_25['WL'] == 'W'].shape[0]
    home_wins_24_25  = home_games_24_25[home_games_24_25['WL'] == 'W'].shape[0]
    road_wins_24_25  = road_games_24_25[road_games_24_25['WL'] == 'W'].shape[0]
    total_wins_23_24 = miami_heat_23_24[miami_heat_23_24['WL'] == 'W'].shape[0]
    home_wins_23_24  = home_games_23_24[home_games_23_24['WL'] == 'W'].shape[0]
    road_wins_23_24  = road_games_23_24[road_games_23_24['WL'] == 'W'].shape[0]

    # Contar derrotas
    total_losses_24_25 = miami_heat_24_25[miami_heat_24_25['WL'] == 'L'].shape[0]
    home_losses_24_25  = home_games_24_25[home_games_24_25['WL'] == 'L'].shape[0]
    road_losses_24_25  = road_games_24_25[road_games_24_25['WL'] == 'L'].shape[0]
    total_losses_23_24 = miami_heat_23_24[miami_heat_23_24['WL'] == 'L'].shape[0]
    home_losses_23_24  = home_games_23_24[home_games_23_24['WL'] == 'L'].shape[0]
    road_losses_23_24  = road_games_23_24[road_games_23_24['WL'] == 'L'].shape[0]

    # Preparar dados para exportação
    data_miami_heat_24_25 = {
        'Total Wins': [total_wins_24_25],
        'Home Wins': [home_wins_24_25],
        'Road Wins': [road_wins_24_25],
        'Total Losses': [total_losses_24_25],
        'Home Losses': [home_losses_24_25],
        'Road Losses': [road_losses_24_25]
    }

    data_miami_heat_23_24 = {
        'Total Wins': [total_wins_23_24],
        'Home Wins': [home_wins_23_24],
        'Road Wins': [road_wins_23_24],
        'Total Losses': [total_losses_23_24],
        'Home Losses': [home_losses_23_24],
        'Road Losses': [road_losses_23_24]
    }

    # Exportando dados
    miami_heat_23_24_summary = pd.DataFrame(data_miami_heat_23_24)
    miami_heat_23_24_summary.to_csv('data/exported/miami_heat_23_24_summary.csv', index=False)
    miami_heat_24_25_summary = pd.DataFrame(data_miami_heat_24_25)
    miami_heat_24_25_summary.to_csv('data/exported/miami_heat_24_25_summary.csv', index=False)

    # Preparar dados para exportação
    total_points_23_24 = miami_heat_23_24['PTS'].sum()
    total_points_24_25 = miami_heat_24_25['PTS'].sum()
    total_assists_23_24 = miami_heat_23_24['AST'].sum()
    total_assists_24_25 = miami_heat_24_25['AST'].sum()
    total_rebounds_23_24 = miami_heat_23_24['REB'].sum()
    total_rebounds_24_25 = miami_heat_24_25['REB'].sum()
    total_3pointers_23_24 = miami_heat_23_24['FG3M'].sum()
    total_3pointers_24_25 = miami_heat_24_25['FG3M'].sum()
    total_home_losses_23_24 = home_games_23_24[home_games_23_24['WL'] == 'L'].shape[0]
    total_home_losses_24_25 = home_games_24_25[home_games_24_25['WL'] == 'L'].shape[0]
    total_road_losses_23_24 = road_games_23_24[road_games_23_24['WL'] == 'L'].shape[0]
    total_road_losses_24_25 = road_games_24_25[road_games_24_25['WL'] == 'L'].shape[0]
    
    # Preparar dados para exportação
    data_miami_heat_pt1_23_24 = {
        'Total Points 23-24': [total_points_23_24],
        'Total Assists 23-24': [total_assists_23_24],
        'Total Rebounds 23-24': [total_rebounds_23_24],
        'Total 3 Points 23-24': [total_3pointers_23_24],
        'Total Home Losses 23-24': [total_home_losses_23_24],
        'Total Road Losses 23-24': [total_road_losses_23_24]
    }

    data_miami_heat_pt1_24_25 = {
        'Total Points 24-25': [total_points_24_25],
        'Total Assists 24-25': [total_assists_24_25],
        'Total Rebounds 24-25': [total_rebounds_24_25],
        'Total 3 Points 24-25': [total_3pointers_24_25],
        'Total Home Losses 24-25': [total_home_losses_24_25],
        'Total Road Losses 24-25': [total_road_losses_24_25]
    }

    # Exportando dados
    miami_heat_summary_23_24_pt1 = pd.DataFrame(data_miami_heat_pt1_23_24)
    miami_heat_summary_23_24_pt1.to_csv('data/exported/miami_heat_summary_23_24_pt1.csv', index=False)
    miami_heat_summary_24_25_pt1 = pd.DataFrame(data_miami_heat_pt1_24_25)
    miami_heat_summary_24_25_pt1.to_csv('data/exported/miami_heat_summary_24_25_pt1.csv', index=False)

    # Preparar dados para exportação
    total_rebounds_23_24 = miami_heat_23_24['REB'].sum()
    total_rebounds_24_25 = miami_heat_24_25['REB'].sum()
    total_offensive_rebounds_23_24 = miami_heat_23_24['OREB'].sum()
    total_offensive_rebounds_24_25 = miami_heat_24_25['OREB'].sum()
    total_defensive_rebounds_23_24 = miami_heat_23_24['DREB'].sum()
    total_defensive_rebounds_24_25 = miami_heat_24_25['DREB'].sum()
    total_points_23_24 = miami_heat_23_24['PTS'].sum()
    total_points_24_25 = miami_heat_24_25['PTS'].sum()
    total_2pointers_23_24 = miami_heat_23_24['FGM'].sum()
    total_2pointers_24_25 = miami_heat_24_25['FGM'].sum()
    total_3pointers_23_24 = miami_heat_23_24['FG3M'].sum()
    total_3pointers_24_25 = miami_heat_24_25['FG3M'].sum()
    total_free_throws_23_24 = miami_heat_23_24['FTM'].sum()
    total_free_throws_24_25 = miami_heat_24_25['FTM'].sum()
    
    # Preparar dados para exportação
    data_miami_heat_pt2_23_24 = {
        'Total Rebounds 23-24': [total_rebounds_23_24],
        'Total Offensive Rebounds 23-24': [total_offensive_rebounds_23_24],
        'Total Defensive Rebounds 23-24': [total_defensive_rebounds_23_24],
        'Total Points 23-24': [total_points_23_24],
        'Total 2 Pointers 23-24': [total_2pointers_23_24],
        'Total 3 Pointers 23-24': [total_3pointers_23_24],
        'Total Free Throws 23-24': [total_free_throws_23_24]
    }

    data_miami_heat_pt2_24_25 = {
        'Total Rebounds 24-25': [total_rebounds_24_25],
        'Total Offensive Rebounds 24-25': [total_offensive_rebounds_24_25],
        'Total Defensive Rebounds 24-25': [total_defensive_rebounds_24_25],
        'Total Points 24-25': [total_points_24_25],
        'Total 2 Pointers 24-25': [total_2pointers_24_25],
        'Total 3 Pointers 24-25': [total_3pointers_24_25],
        'Total Free Throws 24-25': [total_free_throws_24_25]
    }

    # Exportando dados
    miami_heat_summary_23_24_pt2 = pd.DataFrame(data_miami_heat_pt2_23_24)
    miami_heat_summary_23_24_pt2.to_csv('data/exported/miami_heat_summary_23_24_pt2.csv', index=False)
    miami_heat_summary_24_25_pt2 = pd.DataFrame(data_miami_heat_pt2_24_25)
    miami_heat_summary_24_25_pt2.to_csv('data/exported/miami_heat_summary_24_25_pt2.csv', index=False)

    # Preparar dados para exportação
    total_steals_23_24 = miami_heat_23_24['STL'].sum()
    total_steals_24_25 = miami_heat_24_25['STL'].sum()
    total_blocks_23_24 = miami_heat_23_24['BLK'].sum()
    total_blocks_24_25 = miami_heat_24_25['BLK'].sum()
    total_turnovers_23_24 = miami_heat_23_24['TOV'].sum()
    total_turnovers_24_25 = miami_heat_24_25['TOV'].sum()
    total_personal_fouls_23_24 = miami_heat_23_24['PF'].sum()
    total_personal_fouls_24_25 = miami_heat_24_25['PF'].sum()

    # Preparar dados para exportação
    data_miami_heat_defense_23_24 = {
        'Total Steals': [total_steals_23_24],
        'Total Defensive Rebounds': [total_defensive_rebounds_23_24],
        'Total Blocks': [total_blocks_23_24],
        'Total Turnovers': [total_turnovers_23_24],
        'Total Personal Fouls': [total_personal_fouls_23_24]
    }

    data_miami_heat_defense_24_25 = {
        'Total Steals': [total_steals_24_25],
        'Total Defensive Rebounds': [total_defensive_rebounds_24_25],
        'Total Blocks': [total_blocks_24_25],
        'Total Turnovers': [total_turnovers_24_25],
        'Total Personal Fouls': [total_personal_fouls_24_25]
    }

    # Exportando dados
    miami_heat_defensive_summary_23_24 = pd.DataFrame(data_miami_heat_defense_23_24)
    miami_heat_defensive_summary_23_24.to_csv('data/exported/miami_heat_defensive_summary_23_24.csv', index=False)
    miami_heat_defensive_summary_24_25 = pd.DataFrame(data_miami_heat_defense_24_25)
    miami_heat_defensive_summary_24_25.to_csv('data/exported/miami_heat_defensive_summary_24_25.csv', index=False)

    # Apresentar tabela de times
    team_name_map = {
        'ATL': 'Atlanta Hawks', 
        'BOS': 'Boston Celtics', 
        'BKN': 'Brooklyn Nets', 
        'CHA': 'Charlotte Hornets',
        'CHI': 'Chicago Bulls', 'CLE': 
        'Cleveland Cavaliers', 
        'DAL': 'Dallas Mavericks', 
        'DEN': 'Denver Nuggets',
        'DET': 'Detroit miami_heat', 
        'GSW': 'Golden State Warriors', 
        'HOU': 'Houston Rockets', 
        'IND': 'Indiana Pacers',
        'LAC': 'Los Angeles Clippers', 
        'LAL': 'Los Angeles Lakers', 
        'MEM': 'Memphis Grizzlies', 
        'MIA': 'Miami Heat',
        'MIL': 'Milwaukee Bucks', 
        'MIN': 'Minnesota Timberwolves', 
        'NOP': 'New Orleans Pelicans', 
        'NYK': 'New York Knicks',
        'OKC': 'Oklahoma City Thunder', 
        'ORL': 'Orlando Magic', 
        'PHI': 'Philadelphia 76ers', 
        'PHX': 'Phoenix Suns',
        'POR': 'Portland Trail Blazers', 
        'SAC': 'Sacramento Kings', 
        'SAS': 'San Antonio Spurs', 
        'TOR': 'Toronto Raptors',
        'UTA': 'Utah Jazz', 'WAS': 'Washington Wizards'
    }

    # Função para identificar se o jogo é em casa ou fora
    def home_or_road(matchup):
        if "vs" in matchup:
            return "Home"
        elif "@" in matchup:
            return "Road"
        return None
    
    # Função para identificar o adversário
    def get_adversary(matchup):
        if "@" in matchup:
            adversario = matchup.split("@")[1].strip()
        elif "vs" in matchup:
            adversario = matchup.split("vs")[1].strip()
        adversario = adversario.split()[-1]
        return adversario
    
    # Função para identificar o nome do adversário
    def get_adversary_name(adversary):
        return team_name_map.get(adversary, adversary)

    # Função para identificar o placar
    def get_score(pts, plus_minus):
        return f"{pts} - {pts - plus_minus}"
    
    # Apresentar tabela de jogos
    games_23_24 = miami_heat_23_24
    games_24_25 = miami_heat_24_25
    games_all_seasons = miami_heat_all_seasons

    # Apresentar tabela de jogos
    games_23_24['Home or Road'] = games_23_24['MATCHUP'].apply(home_or_road)
    games_23_24['Adversary'] = games_23_24['MATCHUP'].apply(get_adversary)
    games_23_24['Adversary Name'] = games_23_24['Adversary'].apply(get_adversary_name)
    games_23_24['Score'] = games_23_24.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)
    games_24_25['Home or Road'] = games_24_25['MATCHUP'].apply(home_or_road)
    games_24_25['Adversary'] = games_24_25['MATCHUP'].apply(get_adversary)
    games_24_25['Adversary Name'] = games_24_25['Adversary'].apply(get_adversary_name)
    games_24_25['Score'] = games_24_25.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)

    # Apresentar tabela de todos os jogos 
    games_all_seasons['Home or Road'] = games_all_seasons['MATCHUP'].apply(home_or_road)
    games_all_seasons['Adversary'] = games_all_seasons['MATCHUP'].apply(get_adversary)
    games_all_seasons['Adversary Name'] = games_all_seasons['Adversary'].apply(get_adversary_name)
    games_all_seasons['Score'] = games_all_seasons.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)

    # Apresentar tabela de jogadores por temporada
    bam_adebayo_all_seasons['Home or Road'] = bam_adebayo_all_seasons['MATCHUP'].apply(home_or_road)
    bam_adebayo_all_seasons['Adversary'] = bam_adebayo_all_seasons['MATCHUP'].apply(get_adversary)
    tyler_herro_all_seasons['Home or Road'] = tyler_herro_all_seasons['MATCHUP'].apply(home_or_road)
    tyler_herro_all_seasons['Adversary'] = tyler_herro_all_seasons['MATCHUP'].apply(get_adversary)
    jimmy_butler_all_seasons['Home or Road'] = jimmy_butler_all_seasons['MATCHUP'].apply(home_or_road)
    jimmy_butler_all_seasons['Adversary'] = jimmy_butler_all_seasons['MATCHUP'].apply(get_adversary)

    # Filtrar colunas
    games_23_24 = games_23_24[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]
    games_24_25 = games_24_25[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]
    games_all_seasons = games_all_seasons[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]

    # Exportando dados
    games_23_24.to_csv('data/exported/miami_heat_games_table_23_24.csv', index=False)
    games_24_25.to_csv('data/exported/miami_heat_games_table_24_25.csv', index=False)
    games_all_seasons.to_csv('data/exported/miami_heat_games_table_all_seasons.csv', index=False)

    # Armazenar dados dos jogadores    
    bam_adebayo_games_23_24 = bam_adebayo_23_24
    bam_adebayo_games_24_25 = bam_adebayo_24_25
    bam_adebayo_games_all_seasons = bam_adebayo_all_seasons
    tyler_herro_games_23_24 = tyler_herro_23_24
    tyler_herro_games_24_25 = tyler_herro_24_25
    tyler_herro_games_all_seasons = tyler_herro_all_seasons
    jimmy_butler_games_23_24 = jimmy_butler_23_24
    jimmy_butler_games_24_25 = jimmy_butler_24_25
    jimmy_butler_games_all_seasons = jimmy_butler_all_seasons

    # Função para transformar dados dos jogadores
    def transform_player_data(dataset):
        dataset['GAME_DATE'] = pd.to_datetime(dataset['GAME_DATE']).dt.strftime('%Y-%m-%d')
        dataset['Home or Road'] = dataset['MATCHUP'].apply(home_or_road)
        dataset['Adversary'] = dataset['MATCHUP'].apply(get_adversary)
        dataset['Adversary Name'] = dataset['Adversary'].apply(get_adversary_name)
        return dataset
    
    # Função para obter o placar do jogo
    def get_game_score(date, dataset):
        game = dataset[dataset['GAME_DATE'] == date]
        if not game.empty:
            return game.iloc[0]['Score']
        return None
    
    # Transformar dados de Bam Adebayo e adicionar placar do jogo
    bam_adebayo_games_23_24 = transform_player_data(bam_adebayo_games_23_24)
    bam_adebayo_games_24_25 = transform_player_data(bam_adebayo_games_24_25)
    bam_adebayo_games_all_seasons = transform_player_data(bam_adebayo_games_all_seasons)
    bam_adebayo_games_23_24['Game Score'] = bam_adebayo_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
    bam_adebayo_games_24_25['Game Score'] = bam_adebayo_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))
    bam_adebayo_games_all_seasons['Game Score'] = bam_adebayo_games_all_seasons['GAME_DATE'].apply(lambda date: get_game_score(date, games_all_seasons))

    # Transformar dados de Tyler Herro e adicionar placar do jogo
    tyler_herro_games_23_24 = transform_player_data(tyler_herro_23_24)
    tyler_herro_games_24_25 = transform_player_data(tyler_herro_24_25)
    tyler_herro_games_all_seasons = transform_player_data(tyler_herro_all_seasons)
    tyler_herro_games_23_24['Game Score'] = tyler_herro_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
    tyler_herro_games_24_25['Game Score'] = tyler_herro_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))
    tyler_herro_games_all_seasons['Game Score'] = tyler_herro_games_all_seasons['GAME_DATE'].apply(lambda date: get_game_score(date, games_all_seasons))

    # Transformar dados de jimmy Butler e adicionar placar do jogo
    jimmy_butler_games_23_24 = transform_player_data(jimmy_butler_23_24)
    jimmy_butler_games_24_25 = transform_player_data(jimmy_butler_24_25)
    jimmy_butler_games_all_seasons = transform_player_data(jimmy_butler_all_seasons)
    jimmy_butler_games_23_24['Game Score'] = jimmy_butler_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
    jimmy_butler_games_24_25['Game Score'] = jimmy_butler_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))
    jimmy_butler_games_all_seasons['Game Score'] = jimmy_butler_games_all_seasons['GAME_DATE'].apply(lambda date: get_game_score(date, games_all_seasons))

    # Filtrar colunas
    bam_adebayo_games_23_24 = bam_adebayo_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    bam_adebayo_games_24_25 = bam_adebayo_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    tyler_herro_games_23_24 = tyler_herro_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    tyler_herro_games_24_25 = tyler_herro_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    jimmy_butler_games_23_24 = jimmy_butler_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    jimmy_butler_games_24_25 = jimmy_butler_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    bam_adebayo_games_all_seasons_show = bam_adebayo_games_all_seasons[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    tyler_herro_games_all_seasons_show = tyler_herro_games_all_seasons[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    jimmy_butler_games_all_seasons_show = jimmy_butler_games_all_seasons[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]

    # Exportando dados
    bam_adebayo_games_23_24.to_csv('data/exported/bam_adebayo_games_table_23_24.csv', index=False)
    bam_adebayo_games_24_25.to_csv('data/exported/bam_adebayo_games_table_24_25.csv', index=False)
    tyler_herro_games_23_24.to_csv('data/exported/tyler_herro_games_table_23_24.csv', index=False)
    tyler_herro_games_24_25.to_csv('data/exported/tyler_herro_games_table_24_25.csv', index=False)
    jimmy_butler_games_23_24.to_csv('data/exported/jimmy_butler_games_table_23_24.csv', index=False)
    jimmy_butler_games_24_25.to_csv('data/exported/jimmy_butler_games_table_24_25.csv', index=False)
    bam_adebayo_games_all_seasons.to_csv('data/exported/bam_adebayo_games_table_all_seasons.csv', index=False)
    tyler_herro_games_all_seasons.to_csv('data/exported/tyler_herro_games_table_all_seasons.csv', index=False)
    jimmy_butler_games_all_seasons.to_csv('data/exported/jimmy_butler_games_table_all_seasons.csv', index=False)

    # Função para buscar jogos
    def search_games(player_data, search_term):
        search_term = search_term.lower()
        return player_data[player_data['Adversary Name'].str.lower().str.contains(search_term)]
    
    # Solicitar termo de busca
    search_term = input("Digite a equipe adversária: ")

    # Buscar jogos
    bam_adebayo_search_results = search_games(bam_adebayo_games_all_seasons_show, search_term)
    tyler_herro_search_results = search_games(tyler_herro_games_all_seasons_show, search_term)
    jimmy_butler_search_results = search_games(jimmy_butler_games_all_seasons_show, search_term)

    # Verificar se a busca não retornou resultados
    if bam_adebayo_search_results.empty and tyler_herro_search_results.empty and jimmy_butler_search_results.empty:
        print("Não encontrado. Tente novamente.")
        search_term = analisys()
        return search_term
    
    # Exportar dados
    bam_adebayo_search_results.to_csv(f'data/exported/bam_adebayo_games_against_{search_term}.csv', index=False)
    tyler_herro_search_results.to_csv(f'data/exported/tyler_herro_games_against_{search_term}.csv', index=False)
    jimmy_butler_search_results.to_csv(f'data/exported/jimmy_butler_games_against_{search_term}.csv', index=False)

    # Função para calcular médias
    bam_adebayo_vs_magic = search_games(bam_adebayo_games_all_seasons_show, 'magic')
    tyler_herro_vs_magic = search_games(tyler_herro_games_all_seasons_show, 'magic')
    jimmy_butler_vs_magic = search_games(jimmy_butler_games_all_seasons_show, 'magic')

    # Exportar dados
    bam_adebayo_vs_magic.to_csv('data/exported/bam_adebayo_games_vs_magic.csv', index=False)
    tyler_herro_vs_magic.to_csv('data/exported/tyler_herro_games_vs_magic.csv', index=False)
    jimmy_butler_vs_magic.to_csv('data/exported/jimmy_butler_games_vs_magic.csv', index=False)

    # Função para calcular médias
    def calculate_averages(player_data):
        avg_points = player_data['PTS'].mean()
        avg_rebounds = player_data['REB'].mean()
        avg_assists = player_data['AST'].mean()
        return avg_points, avg_rebounds, avg_assists
    
    # Função para calcular medianas
    def calculate_medians(player_data):
        median_points = player_data['PTS'].median()
        median_rebounds = player_data['REB'].median()
        median_assists = player_data['AST'].median()
        return median_points, median_rebounds, median_assists
    
    # Função para calcular modas
    def calculate_modes(player_data):
        mode_points = player_data['PTS'].mode()[0]
        mode_rebounds = player_data['REB'].mode()[0]
        mode_assists = player_data['AST'].mode()[0]
        return mode_points, mode_rebounds, mode_assists
    
    # Função para calcular porcentagem abaixo da média
    def calculate_below_average_percentage(player_data, avg_points, avg_rebounds, avg_assists):
        below_avg_points = (player_data['PTS'] < avg_points).mean() * 100
        below_avg_rebounds = (player_data['REB'] < avg_rebounds).mean() * 100
        below_avg_assists = (player_data['AST'] < avg_assists).mean() * 100
        return below_avg_points, below_avg_rebounds, below_avg_assists
    
    # Função para calcular porcentagem abaixo da mediana
    def calculate_below_median_percentage(player_data, median_points, median_rebounds, median_assists):
        below_median_points = (player_data['PTS'] < median_points).mean() * 100
        below_median_rebounds = (player_data['REB'] < median_rebounds).mean() * 100
        below_median_assists = (player_data['AST'] < median_assists).mean() * 100
        return below_median_points, below_median_rebounds, below_median_assists
    
    # Função para calcular porcentagem abaixo da moda
    def calculate_below_mode_percentage(player_data, mode_points, mode_rebounds, mode_assists):
        below_mode_points = (player_data['PTS'] < mode_points).mean() * 100
        below_mode_rebounds = (player_data['REB'] < mode_rebounds).mean() * 100
        below_mode_assists = (player_data['AST'] < mode_assists).mean() * 100
        return below_mode_points, below_mode_rebounds, below_mode_assists
    
    # Função para calcular desvios padrão
    def calculate_standard_deviations(player_data):
        std_points = player_data['PTS'].std()
        std_rebounds = player_data['REB'].std()
        std_assists = player_data['AST'].std()
        return std_points, std_rebounds, std_assists
    
    # Função para exibir estatísticas dos jogadores
    def display_player_stats(player_data, player_name):
        avg_points, avg_rebounds, avg_assists = calculate_averages(player_data)
        median_points, median_rebounds, median_assists = calculate_medians(player_data)
        mode_points, mode_rebounds, mode_assists = calculate_modes(player_data)
        below_avg_points, below_avg_rebounds, below_avg_assists = calculate_below_average_percentage(player_data, avg_points, avg_rebounds, avg_assists)
        below_median_points, below_median_rebounds, below_median_assists = calculate_below_median_percentage(player_data, median_points, median_rebounds, median_assists)
        below_mode_points, below_mode_rebounds, below_mode_assists = calculate_below_mode_percentage(player_data, mode_points, mode_rebounds, mode_assists)
        std_points, std_rebounds, std_assists = calculate_standard_deviations(player_data)
        total_games = player_data.shape[0]

        # Armazenar dados
        stats_data = {
            'Player Name': [player_name],
            'Total Games': [total_games],
            'Average Points': [avg_points],
            'Median Points': [median_points],
            'Mode Points': [mode_points],
            'Standard Deviation Points': [std_points],
            'Average Rebounds': [avg_rebounds],
            'Median Rebounds': [median_rebounds],
            'Mode Rebounds': [mode_rebounds],
            'Standard Deviation Rebounds': [std_rebounds],
            'Average Assists': [avg_assists],
            'Median Assists': [median_assists],
            'Mode Assists': [mode_assists],
            'Standard Deviation Assists': [std_assists],
            'Below Average Points (%)': [below_avg_points],
            'Below Average Rebounds (%)': [below_avg_rebounds],
            'Below Average Assists (%)': [below_avg_assists],
            'Below Median Points (%)': [below_median_points],
            'Below Median Rebounds (%)': [below_median_rebounds],
            'Below Median Assists (%)': [below_median_assists],
            'Below Mode Points (%)': [below_mode_points],
            'Below Mode Rebounds (%)': [below_mode_rebounds],
            'Below Mode Assists (%)': [below_mode_assists]
        }

        # Exportar dados
        stats_df = pd.DataFrame(stats_data)
        stats_df.to_csv(f'data/exported/{player_name.replace(" ", "_").lower()}_stats.csv', index=False)

    # Exibir estatísticas dos jogadores
    display_player_stats(bam_adebayo_games_23_24, "bam_adebayo_23_24")
    display_player_stats(bam_adebayo_games_24_25, "bam_adebayo_24_25")
    display_player_stats(tyler_herro_games_23_24, "tyler_herro 23-24")
    display_player_stats(tyler_herro_games_24_25, "tyler_herro 24-25")
    display_player_stats(jimmy_butler_games_23_24, "jimmy_butler 23-24")
    display_player_stats(jimmy_butler_games_24_25, "jimmy_butler 24-25")
    display_player_stats(bam_adebayo_games_all_seasons, "bam_adebayo_all_seasons")
    display_player_stats(tyler_herro_games_all_seasons, "tyler_herro_all_seasons")
    display_player_stats(jimmy_butler_games_all_seasons, "jimmy_butler_all_seasons")

    # Função para criar dataset combinado
    def create_combined_dataset(player_all_seasons, player_24_25, player_name):
        # Calcular totais
        total_games_all_seasons = player_all_seasons.shape[0]
        total_points_all_seasons = player_all_seasons['PTS'].sum()
        total_assists_all_seasons = player_all_seasons['AST'].sum()
        total_rebounds_all_seasons = player_all_seasons['REB'].sum()
        total_minutes_all_seasons = player_all_seasons['MIN'].sum()

        # Armazenar dados
        total_games_24_25 = player_24_25.shape[0]
        total_points_24_25 = player_24_25['PTS'].sum()
        total_assists_24_25 = player_24_25['AST'].sum()
        total_rebounds_24_25 = player_24_25['REB'].sum()
        total_minutes_24_25 = player_24_25['MIN'].sum()

        # Armazenar dados
        combined_data = {
            'Estatisticas': ['Carreira', 'Temporada Atual'],
            'Total de Jogos': [total_games_all_seasons, total_games_24_25],
            'Total de Pontos': [total_points_all_seasons, total_points_24_25],
            'Total de Assistências': [total_assists_all_seasons, total_assists_24_25],
            'Total de Rebotes': [total_rebounds_all_seasons, total_rebounds_24_25],
            'Total de Minutos em Quadra': [total_minutes_all_seasons, total_minutes_24_25]
        }

        # Exportar dados
        combined_df = pd.DataFrame(combined_data)
        combined_df.to_csv(f'data/exported/{player_name.replace(" ", "_").lower()}_combined_stats.csv', index=False)

    # Criar dataset combinado
    create_combined_dataset(bam_adebayo_games_all_seasons, bam_adebayo_games_24_25, "bam_adebayo")
    create_combined_dataset(tyler_herro_games_all_seasons, tyler_herro_games_24_25, "tyler_herro")
    create_combined_dataset(jimmy_butler_games_all_seasons, jimmy_butler_games_24_25, "jimmy_butler")

    # Função para exibir estatísticas dos jogadores
    return search_term