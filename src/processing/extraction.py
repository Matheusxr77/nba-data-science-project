# Importando bibliotecas
import requests
import pandas as pd
import datetime
from nba_api.stats.endpoints import commonteamroster, LeagueStandings, LeagueGameLog
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog

# Função para extrair dados
def extraction():
    # Extraindo dados dos times
    nba_teams = teams.get_teams()

    # Extraindo dados do Miami Heat
    miami_heat = [team for team in nba_teams if team['full_name'] == 'Miami Heat'][0]
    miami_heat_id = miami_heat['id']

    # Extraindo dados de classificação por conferência
    standings = LeagueStandings()
    standings_data = standings.get_data_frames()[0]
    selected_columns = ['TeamID', 'TeamName', 'Conference', 'WINS', 'LOSSES', 'WinPCT', 'HOME', 'ROAD', 'L10', 'CurrentStreak']
    selected_standings_data = standings_data[selected_columns]

    # Salvando dados de classificação por conferência
    east_conference = selected_standings_data[selected_standings_data['Conference'] == 'East']
    east_conference_sorted = east_conference.sort_values(by='WINS', ascending=False)

    west_conference = selected_standings_data[selected_standings_data['Conference'] == 'West']
    west_conference_sorted = west_conference.sort_values(by='WINS', ascending=False)

    # Salvando dados de classificação por conferência
    east_conference_sorted.to_csv('data/raw/east_conference.csv', index=False)
    west_conference_sorted.to_csv('data/raw/west_conference.csv', index=False)

    # Extraindo dados do time Miami Heat
    def get_games_by_season(season):
        # Extraindo dados dos jogos da temporada
        game_log = LeagueGameLog(season=season)

        # Selecionando apenas os jogos do Miami Heat
        games = game_log.get_data_frames()[0]

        return games
    
    # Extraindo dados dos jogos da temporada
    games_21_22 = get_games_by_season("2021-22")
    games_22_23 = get_games_by_season("2022-23")
    games_23_24 = get_games_by_season("2023-24")
    games_24_25 = get_games_by_season("2024-25")
    
    # Selecionando apenas os jogos do Miami Heat
    miami_heat_games_21_22 = games_21_22[games_21_22["TEAM_NAME"] == "Miami Heat"]
    miami_heat_games_22_23 = games_22_23[games_22_23["TEAM_NAME"] == "Miami Heat"]
    miami_heat_games_23_24 = games_23_24[games_23_24["TEAM_NAME"] == "Miami Heat"]
    miami_heat_games_24_25 = games_24_25[games_24_25["TEAM_NAME"] == "Miami Heat"]
    
    # Salvando dados dos jogos do Miami Heat
    miami_heat_games_21_22.to_csv('data/raw/miami_heat_games_21_22.csv', index=False)
    miami_heat_games_22_23.to_csv('data/raw/miami_heat_games_22_23.csv', index=False)
    miami_heat_games_23_24.to_csv('data/raw/miami_heat_games_23_24.csv', index=False)
    miami_heat_games_24_25.to_csv('data/raw/miami_heat_games_24_25.csv', index=False)
    
    # Extraindo dados dos jogadores do Miami Heat
    players = ['Bam Adebayo', 'Tyler Herro', 'Jimmy Butler']

    # Extraindo dados dos jogos dos jogadores
    player_stats_23_24 = {}
    player_stats_24_25 = {}

    # Extraindo dados dos jogos dos jogadores do Miami Heat
    for player in players:
        # Extraindo ID do jogador
        player_id = commonteamroster.CommonTeamRoster(team_id=miami_heat_id, season="2023-24").get_data_frames()[0]
        player_id = player_id[player_id['PLAYER'].str.contains(player)]['PLAYER_ID'].values[0]

        # Extraindo dados dos jogos do jogador na temporada 2023-24
        player_game_log_23_24 = playergamelog.PlayerGameLog(player_id=player_id, season="2023-24")
        player_stats_23_24[player] = player_game_log_23_24.get_data_frames()[0]

        # Extraindo dados dos jogos do jogador na temporada 2024-25
        player_game_log_24_25 = playergamelog.PlayerGameLog(player_id=player_id, season="2024-25")
        player_stats_24_25[player] = player_game_log_24_25.get_data_frames()[0]

    # Salvando dados dos jogos dos jogadores
    for player in players:
        player_stats_23_24[player].to_csv(f'data/raw/{player.lower().replace(" ", "_")}_stats_23_24.csv', index=False)
        player_stats_24_25[player].to_csv(f'data/raw/{player.lower().replace(" ", "_")}_stats_24_25.csv', index=False)

    # Extraindo dados dos jogadores
    url = "https://stats.nba.com/stats/commonplayerinfo"

    # Headers da requisição
    headers = {
        "Host": "stats.nba.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.nba.com",
        "Referer": "https://www.nba.com/",
        "Connection": "keep-alive",
    }

    # IDs dos jogadores
    players = {
        "Bam Adebayo": "1628389",
        "Tyler Herro": "1629639",
        "Jimmy Butler": "202710"
    }

    # Função para calcular a idade dos jogadores
    def calculate_age(birthdate_str):
        birthdate = datetime.datetime.strptime(birthdate_str.split("T")[0], "%Y-%m-%d")
        today = datetime.datetime.today()

        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Extraindo informações dos jogadores
    player_info = []

    # Extraindo informações dos jogadores pelo ID
    for player_name, player_id in players.items():
        # Parâmetros da requisição
        params = {"PlayerID": player_id}
        
        # Requisição para extrair informações dos jogadores
        try:
            # Fazendo a requisição
            response = requests.get(url, headers=headers, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()

            # Extraindo informações dos jogadores
            player_data = data['resultSets'][0]['rowSet'][0]
            response_headers = data['resultSets'][0]['headers']
            player_dict = dict(zip(response_headers, player_data))

            # Dados da idade do jogador
            birthdate = player_dict.get("BIRTHDATE", "1900-01-01")
            idade = calculate_age(birthdate) if birthdate != "1900-01-01" else "Desconhecido"

            # Dados dos jogadores
            selected_data = {
                "ID": player_id,
                "Nome": player_dict.get("DISPLAY_FIRST_LAST"),
                "Altura": player_dict.get("HEIGHT"),
                "Peso": player_dict.get("WEIGHT"),
                "Idade": idade,
                "Experiência": player_dict.get("SEASON_EXP"),
                "Posição": player_dict.get("POSITION"),
                "Universidade": player_dict.get("SCHOOL"),
                "Salário": player_dict.get("SALARY", "Não disponível")
            }

            # Adicionando dados dos jogadores
            player_info.append(selected_data)
        
        # Tratamento de erro
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar dados do jogador {player_name}: {e}")

    # Salvando dados dos jogadores
    for player in player_info:
        player_name = player["Nome"]
        player_stats_df = pd.DataFrame([player])
        player_stats_df.to_csv(f"data/raw/{player_name.replace(' ', '_')}_profile.csv", index=False)

    # Extraindo dados dos jogos de todas as temporadas
    all_seasons = ["2021-22", "2022-23", "2023-24", "2024-25"]

    # Extraindo dados dos jogadores
    all_player_stats = {}

    # Extraindo dados dos jogos
    for player in players:
        # Extraindo ID do jogador 
        player_id = commonteamroster.CommonTeamRoster(team_id=miami_heat_id, season="2023-24").get_data_frames()[0]
        player_id = player_id[player_id['PLAYER'].str.contains(player)]['PLAYER_ID'].values[0]

        # Inicializando DataFrame
        all_player_stats[player] = pd.DataFrame()

        # Extraindo dados dos jogos do jogador em todas as temporadas
        for season in all_seasons:
            player_game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
            season_stats = player_game_log.get_data_frames()[0]
            season_stats['SEASON'] = season
            all_player_stats[player] = pd.concat([all_player_stats[player], season_stats], ignore_index=True)

    # Salvando dados dos jogos dos jogadores
    for player in players:
        all_player_stats[player].to_csv(f'data/raw/{player.lower().replace(" ", "_")}_all_seasons_games.csv', index=False)