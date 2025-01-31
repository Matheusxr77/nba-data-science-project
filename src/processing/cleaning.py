# Importando bibliotecas
import pandas as pd

# Função para realizar a limpeza os dados
def cleaning():
    # Carregar dados brutos
    miami_heat_21_22 = pd.read_csv('data/raw/miami_heat_games_21_22.csv')
    miami_heat_22_23 = pd.read_csv('data/raw/miami_heat_games_22_23.csv')
    miami_heat_23_24 = pd.read_csv('data/raw/miami_heat_games_23_24.csv')
    miami_heat_24_25 = pd.read_csv('data/raw/miami_heat_games_24_25.csv')
    west_conference = pd.read_csv('data/raw/west_conference.csv')
    east_conference = pd.read_csv('data/raw/east_conference.csv')
    bam_adebayo_23_24 = pd.read_csv('data/raw/bam_adebayo_stats_23_24.csv')
    bam_adebayo_24_25 = pd.read_csv('data/raw/bam_adebayo_stats_24_25.csv')
    bam_adebayo_all_seasons = pd.read_csv('data/raw/bam_adebayo_all_seasons_games.csv')
    bam_adebayo_profile = pd.read_csv('data/raw/Bam_Adebayo_profile.csv')
    tyler_herro_23_24 = pd.read_csv('data/raw/tyler_herro_stats_23_24.csv')
    tyler_herro_24_25 = pd.read_csv('data/raw/tyler_herro_stats_24_25.csv')
    tyler_herro_all_seasons = pd.read_csv('data/raw/tyler_herro_all_seasons_games.csv')
    tyler_herro_profile = pd.read_csv('data/raw/Tyler_Herro_profile.csv')
    jimmy_butler_23_24 = pd.read_csv('data/raw/jimmy_butler_stats_23_24.csv')
    jimmy_butler_24_25 = pd.read_csv('data/raw/jimmy_butler_stats_24_25.csv')
    jimmy_butler_all_seasons = pd.read_csv('data/raw/jimmy_butler_all_seasons_games.csv')
    jimmy_butler_profile = pd.read_csv('data/raw/Jimmy_Butler_profile.csv')

    # Verificar dados ausentes e Lidando com eles
    missing_data_bam_adebayo = bam_adebayo_23_24.isnull().sum() + bam_adebayo_24_25.isnull().sum() + bam_adebayo_all_seasons.isnull().sum()
    missing_data_tyler_herro = tyler_herro_23_24.isnull().sum() + tyler_herro_24_25.isnull().sum() + tyler_herro_all_seasons.isnull().sum()
    missing_data_jimmy_butler = jimmy_butler_23_24.isnull().sum() + jimmy_butler_24_25.isnull().sum() + jimmy_butler_all_seasons.isnull().sum()
    missing_data_miami_heat = miami_heat_23_24.isnull().sum() + miami_heat_24_25.isnull().sum() + miami_heat_21_22.isnull().sum() + miami_heat_22_23.isnull().sum()
    missing_data_east = east_conference.isnull().sum()
    missing_data_west = west_conference.isnull().sum()

    # Verificar se há dados ausentes
    if missing_data_bam_adebayo.any() > 0:
        print("Bam Adebayo tem conjuntos de dados com dados ausentes.")
    if missing_data_tyler_herro.any() > 0:
        print("Tyler Herro tem conjuntos de dados com dados ausentes.")
    if missing_data_jimmy_butler.any() > 0:
        print("Jimmy Butler tem conjuntos de dados com dados ausentes.")
    if missing_data_miami_heat.any() > 0:
        print("Miami Heat tem conjuntos de dados com dados ausentes.")
    if missing_data_east.any() > 0:
        print("Conferência Leste tem conjuntos de dados com dados ausentes.")
    if missing_data_west.any() > 0:
        print("Conferância Oeste tem conjuntos de dados com dados ausentes.")

    # Lidando com dados ausentes
    def handle_missing_data(df):
        return df.dropna()
    
    # Verificando se há dados ausentes e lidando com eles
    if missing_data_bam_adebayo.any():
        bam_adebayo_23_24 = handle_missing_data(bam_adebayo_23_24)
        bam_adebayo_24_25 = handle_missing_data(bam_adebayo_24_25)
        bam_adebayo_all_seasons = handle_missing_data(bam_adebayo_all_seasons)
    if missing_data_tyler_herro.any():
        tyler_herro_23_24 = handle_missing_data(tyler_herro_23_24)
        tyler_herro_24_25 = handle_missing_data(tyler_herro_24_25)
        tyler_herro_all_seasons = handle_missing_data(tyler_herro_all_seasons)
    if missing_data_jimmy_butler.any():
        jimmy_butler_23_24 = handle_missing_data(jimmy_butler_23_24)
        jimmy_butler_24_25 = handle_missing_data(jimmy_butler_24_25)
        jimmy_butler_all_seasons = handle_missing_data(jimmy_butler_all_seasons)
    if missing_data_miami_heat.any():
        miami_heat_23_24 = handle_missing_data(miami_heat_23_24)
        miami_heat_24_25 = handle_missing_data(miami_heat_24_25)
        miami_heat_21_22 = handle_missing_data(miami_heat_21_22)
        miami_heat_22_23 = handle_missing_data(miami_heat_22_23)

    # Verificar valores duplicados
    redundant_data_bam_adebayo = bam_adebayo_23_24.duplicated().sum() + bam_adebayo_24_25.duplicated().sum() + bam_adebayo_all_seasons.duplicated().sum()
    redundant_data_tyler_herro = tyler_herro_23_24.duplicated().sum() + tyler_herro_24_25.duplicated().sum() + tyler_herro_all_seasons.duplicated().sum()
    redundant_data_jimmy_butler = jimmy_butler_23_24.duplicated().sum() + jimmy_butler_24_25.duplicated().sum() + jimmy_butler_all_seasons.duplicated().sum()
    redundant_data_miami_heat = miami_heat_23_24.duplicated().sum() + miami_heat_24_25.duplicated().sum() + miami_heat_21_22.duplicated().sum() + miami_heat_22_23.duplicated().sum()
    redundant_data_east = east_conference.duplicated().sum()
    redundant_data_west = west_conference.duplicated().sum()

    if redundant_data_bam_adebayo > 0:
        print("Bam Adebayo tem dados redundantes")
    if redundant_data_tyler_herro > 0:
        print("Tyler Herro tem dados redundantes")
    if redundant_data_jimmy_butler > 0:
        print("Jimmy Butler tem dados redundantes")
    if redundant_data_miami_heat > 0:
        print("Miami Heat tem dados redundantes")
    if redundant_data_east > 0:
        print("Conferência Leste tem dados redundantes.")
    if redundant_data_west > 0:
        print("Conferência Oeste tem dados redundantes.")

    # Lidando com dados duplicados
    def handle_duplicates(df):
        return df.drop_duplicates()
    
    # Verificando se há dados duplicados e lidando com eles
    if redundant_data_bam_adebayo.any():
        bam_adebayo_23_24 = handle_duplicates(bam_adebayo_23_24)
        bam_adebayo_24_25 = handle_duplicates(bam_adebayo_24_25)
        bam_adebayo_all_seasons = handle_duplicates(bam_adebayo_all_seasons)
    if redundant_data_tyler_herro.any():
        tyler_herro_23_24 = handle_duplicates(tyler_herro_23_24)
        tyler_herro_24_25 = handle_duplicates(tyler_herro_24_25)
        tyler_herro_all_seasons = handle_duplicates(tyler_herro_all_seasons)
    if redundant_data_jimmy_butler.any():
        jimmy_butler_23_24 = handle_duplicates(jimmy_butler_23_24)
        jimmy_butler_24_25 = handle_duplicates(jimmy_butler_24_25)
        jimmy_butler_all_seasons = handle_duplicates(jimmy_butler_all_seasons)
    if redundant_data_miami_heat.any():
        miami_heat_23_24 = handle_duplicates(miami_heat_23_24)
        miami_heat_24_25 = handle_duplicates(miami_heat_24_25)
        miami_heat_21_22 = handle_duplicates(miami_heat_21_22)
        miami_heat_22_23 = handle_duplicates(miami_heat_22_23)

    # Verificar valores negativos fora de contexto
    def check_negative_values(df, columns):
        return df[columns].lt(0).sum()
    
    # Verificar valores negativos fora de contexto
    negative_values_bam_adebayo = check_negative_values(bam_adebayo_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(bam_adebayo_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(bam_adebayo_all_seasons, ['PTS', 'REB', 'AST'])
    negative_values_tyler_herro = check_negative_values(tyler_herro_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(tyler_herro_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(tyler_herro_all_seasons, ['PTS', 'REB', 'AST'])
    negative_values_jimmy_butler = check_negative_values(jimmy_butler_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(jimmy_butler_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(jimmy_butler_all_seasons, ['PTS', 'REB', 'AST'])
    negative_values_miami_heat = check_negative_values(miami_heat_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(miami_heat_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(miami_heat_21_22, ['PTS', 'REB', 'AST']) + check_negative_values(miami_heat_22_23, ['PTS', 'REB', 'AST'])

    if negative_values_bam_adebayo.any() > 0:
        print("Bam Adebayo tem conjunto de dados com valores negativos fora de contexto.")
    if negative_values_tyler_herro.any() > 0:
        print("Tyler Herro tem conjunto de dados com valores negativos fora de contexto.")
    if negative_values_jimmy_butler.any() > 0:
        print("Jimmy Butler tem conjunto de dados com valores negativos fora de contexto.")
    if negative_values_miami_heat.any() > 0:
        print("Miami Heat tem conjunto de dados com valores negativos fora de contexto.")

    # Lidando com valores negativos
    def handle_negative_values(df, columns):
        for column in columns:
            df[column] = df[column].apply(lambda x: 0 if x < 0 else x)
        return df
    
    # Lidando com valores negativos fora de contexto 
    if negative_values_bam_adebayo.any():
        bam_adebayo_23_24 = handle_negative_values(bam_adebayo_23_24, ['PTS', 'REB', 'AST'])
        bam_adebayo_24_25 = handle_negative_values(bam_adebayo_24_25, ['PTS', 'REB', 'AST'])
        bam_adebayo_all_seasons = handle_negative_values(bam_adebayo_all_seasons, ['PTS', 'REB', 'AST'])
    if negative_values_tyler_herro.any():
        tyler_herro_23_24 = handle_negative_values(tyler_herro_23_24, ['PTS', 'REB', 'AST'])
        tyler_herro_24_25 = handle_negative_values(tyler_herro_24_25, ['PTS', 'REB', 'AST'])
        tyler_herro_all_seasons = handle_negative_values(tyler_herro_all_seasons, ['PTS', 'REB', 'AST'])
    if negative_values_jimmy_butler.any():
        jimmy_butler_23_24 = handle_negative_values(jimmy_butler_23_24, ['PTS', 'REB', 'AST'])
        jimmy_butler_24_25 = handle_negative_values(jimmy_butler_24_25, ['PTS', 'REB', 'AST'])
        jimmy_butler_all_seasons = handle_negative_values(jimmy_butler_all_seasons, ['PTS', 'REB', 'AST'])
    if negative_values_miami_heat.any():
        miami_heat_23_24 = handle_negative_values(miami_heat_23_24, ['PTS', 'REB', 'AST'])
        miami_heat_24_25 = handle_negative_values(miami_heat_24_25, ['PTS', 'REB', 'AST'])
        miami_heat_21_22 = handle_negative_values(miami_heat_21_22, ['PTS', 'REB', 'AST'])
        miami_heat_22_23 = handle_negative_values(miami_heat_22_23, ['PTS', 'REB', 'AST'])

    # Verificar porcentagens que não estão entre 0 e 1
    def check_percentage_values(df, columns):
        return df[columns].apply(lambda x: (x < 0) | (x > 1)).sum()
    
    # Verificar porcentagens fora do intervalo
    percentage_columns = ['FG3_PCT', 'FG_PCT', 'FT_PCT']
    percentage_values_bam_adebayo = check_percentage_values(bam_adebayo_23_24, percentage_columns) + check_percentage_values(bam_adebayo_24_25, percentage_columns) + check_percentage_values(bam_adebayo_all_seasons, percentage_columns)
    percentage_values_tyler_herro = check_percentage_values(tyler_herro_23_24, percentage_columns) + check_percentage_values(tyler_herro_24_25, percentage_columns) + check_percentage_values(tyler_herro_all_seasons, percentage_columns)
    percentage_values_jimmy_butler = check_percentage_values(jimmy_butler_23_24, percentage_columns) + check_percentage_values(jimmy_butler_24_25, percentage_columns) + check_percentage_values(jimmy_butler_all_seasons, percentage_columns)
    percentage_values_miami_heat = check_percentage_values(miami_heat_23_24, percentage_columns) + check_percentage_values(miami_heat_24_25, percentage_columns) + check_percentage_values(miami_heat_21_22, percentage_columns) + check_percentage_values(miami_heat_22_23, percentage_columns)

    # Verificar porcentagens fora do intervalo
    if percentage_values_bam_adebayo.any() > 0:
        print("Bam Adebayo tem conjunto de dados com porcentagem fora de intervalo.")
    if percentage_values_tyler_herro.any() > 0:
        print("Tyler Herro tem conjunto de dados com porcentagem fora de intervalo.")
    if percentage_values_jimmy_butler.any() > 0:
        print("Jimmy Butler tem conjunto de dados com porcentagem fora de intervalo.")
    if percentage_values_miami_heat.any() > 0:
        print("Miami Heat tem conjunto de dados com porcentagem fora de intervalo.")

    # Lidando com porcentagens fora do intervalo
    def handle_percentage_values(df, columns):
        for column in columns:
            df[column] = df[column].apply(lambda x: 0 if x < 0 else 1 if x > 1 else x)
        return df
    
    # Lidando com porcentagens fora do intervalo
    if percentage_values_bam_adebayo.any():
        bam_adebayo_23_24 = handle_percentage_values(bam_adebayo_23_24, percentage_columns)
        bam_adebayo_24_25 = handle_percentage_values(bam_adebayo_24_25, percentage_columns)
        bam_adebayo_all_seasons = handle_percentage_values(bam_adebayo_all_seasons, percentage_columns)
    if percentage_values_tyler_herro.any():
        tyler_herro_23_24 = handle_percentage_values(tyler_herro_23_24, percentage_columns)
        tyler_herro_24_25 = handle_percentage_values(tyler_herro_24_25, percentage_columns)
        tyler_herro_all_seasons = handle_percentage_values(tyler_herro_all_seasons, percentage_columns)
    if percentage_values_jimmy_butler.any():
        jimmy_butler_23_24 = handle_percentage_values(jimmy_butler_23_24, percentage_columns)
        jimmy_butler_24_25 = handle_percentage_values(jimmy_butler_24_25, percentage_columns)
        jimmy_butler_all_seasons = handle_percentage_values(jimmy_butler_all_seasons, percentage_columns)

    # Verificando tipos de dados
    def check_data_types(df):
        return df.dtypes
    
    # Remoção de dados desnecessários
    # Excluindo a coluna "VIDEO_AVAILABLE" dos datasets de jogadores
    bam_adebayo_23_24 = bam_adebayo_23_24.drop(columns=['VIDEO_AVAILABLE'])
    bam_adebayo_24_25 = bam_adebayo_24_25.drop(columns=['VIDEO_AVAILABLE'])
    bam_adebayo_all_seasons = bam_adebayo_all_seasons.drop(columns=['VIDEO_AVAILABLE'])
    tyler_herro_23_24 = tyler_herro_23_24.drop(columns=['VIDEO_AVAILABLE'])
    tyler_herro_24_25 = tyler_herro_24_25.drop(columns=['VIDEO_AVAILABLE'])
    tyler_herro_all_seasons = tyler_herro_all_seasons.drop(columns=['VIDEO_AVAILABLE'])
    jimmy_butler_23_24 = jimmy_butler_23_24.drop(columns=['VIDEO_AVAILABLE'])
    jimmy_butler_24_25 = jimmy_butler_24_25.drop(columns=['VIDEO_AVAILABLE'])
    jimmy_butler_all_seasons = jimmy_butler_all_seasons.drop(columns=['VIDEO_AVAILABLE'])

    # Excluindo a coluna "Team_ID" dos datasets de time
    miami_heat_23_24 = miami_heat_23_24.drop(columns=['TEAM_ID'])
    miami_heat_24_25 = miami_heat_24_25.drop(columns=['TEAM_ID'])
    miami_heat_21_22 = miami_heat_21_22.drop(columns=['TEAM_ID'])
    miami_heat_22_23 = miami_heat_22_23.drop(columns=['TEAM_ID'])

    # Excluindo a coluna "VIDEO_AVAILABLE" dos datasets de time
    miami_heat_23_24 = miami_heat_23_24.drop(columns=['VIDEO_AVAILABLE'])
    miami_heat_24_25 = miami_heat_24_25.drop(columns=['VIDEO_AVAILABLE'])
    miami_heat_21_22 = miami_heat_21_22.drop(columns=['VIDEO_AVAILABLE'])
    miami_heat_22_23 = miami_heat_22_23.drop(columns=['VIDEO_AVAILABLE'])

    # Excluinto a coluna "SEASON_ID" dos datasets de time
    miami_heat_23_24 = miami_heat_23_24.drop(columns=['SEASON_ID'])
    miami_heat_24_25 = miami_heat_24_25.drop(columns=['SEASON_ID'])
    miami_heat_21_22 = miami_heat_21_22.drop(columns=['SEASON_ID'])
    miami_heat_22_23 = miami_heat_22_23.drop(columns=['SEASON_ID'])

    # Excluindo a coluna "TEAM_ABBREVIATION" dos datasets de time
    miami_heat_23_24 = miami_heat_23_24.drop(columns=['TEAM_ABBREVIATION'])
    miami_heat_24_25 = miami_heat_24_25.drop(columns=['TEAM_ABBREVIATION'])
    miami_heat_21_22 = miami_heat_21_22.drop(columns=['TEAM_ABBREVIATION'])
    miami_heat_22_23 = miami_heat_22_23.drop(columns=['TEAM_ABBREVIATION'])

    # Excluindo a coluna "TEAM_NAME" dos datasets de time
    miami_heat_23_24 = miami_heat_23_24.drop(columns=['TEAM_NAME'])
    miami_heat_24_25 = miami_heat_24_25.drop(columns=['TEAM_NAME'])
    miami_heat_21_22 = miami_heat_21_22.drop(columns=['TEAM_NAME'])
    miami_heat_22_23 = miami_heat_22_23.drop(columns=['TEAM_NAME'])

    # Excluindo a coluna "Conference" dos datasets de conferencia
    west_conference = west_conference.drop(columns=['Conference'])
    east_conference = east_conference.drop(columns=['Conference'])

    # Convertendo o peso dos jogadores de Pounds para Quilogramas
    def pounds_to_kg(pounds):
        return round(pounds * 0.453592, 2)
    
    # Convertendo o peso dos jogadores de libras para quilogramas
    bam_adebayo_profile['Peso'] = bam_adebayo_profile['Peso'].apply(pounds_to_kg)
    tyler_herro_profile['Peso'] = tyler_herro_profile['Peso'].apply(pounds_to_kg)
    jimmy_butler_profile['Peso'] = jimmy_butler_profile['Peso'].apply(pounds_to_kg)

    # Convertendo a altura dos jogadores de feets para metros
    def feet_inches_to_meters(height):
        feet, inches = map(int, height.split('-'))
        return round(feet * 0.3048 + inches * 0.0254, 2)
    
    # Convertendo a altura dos jogadores de pés para metros
    bam_adebayo_profile['Altura'] = bam_adebayo_profile['Altura'].apply(feet_inches_to_meters)
    tyler_herro_profile['Altura'] = tyler_herro_profile['Altura'].apply(feet_inches_to_meters)
    jimmy_butler_profile['Altura'] = jimmy_butler_profile['Altura'].apply(feet_inches_to_meters)

    # Salvar dados limpos
    bam_adebayo_23_24.to_csv('data/processed/bam_adebayo_stats_23_24.csv', index=False)
    bam_adebayo_24_25.to_csv('data/processed/bam_adebayo_stats_24_25.csv', index=False)
    bam_adebayo_all_seasons.to_csv('data/processed/bam_adebayo_all_seasons_games.csv', index=False)
    tyler_herro_23_24.to_csv('data/processed/tyler_herro_stats_23_24.csv', index=False)
    tyler_herro_24_25.to_csv('data/processed/tyler_herro_stats_24_25.csv', index=False)
    tyler_herro_all_seasons.to_csv('data/processed/tyler_herro_all_seasons_games.csv', index=False)
    jimmy_butler_23_24.to_csv('data/processed/jimmy_butler_stats_23_24.csv', index=False)
    jimmy_butler_24_25.to_csv('data/processed/jimmy_butler_stats_24_25.csv', index=False)
    jimmy_butler_all_seasons.to_csv('data/processed/jimmy_butler_all_seasons_games.csv', index=False)
    miami_heat_23_24.to_csv('data/processed/miami_heat_games_23_24.csv', index=False)
    miami_heat_24_25.to_csv('data/processed/miami_heat_games_24_25.csv', index=False)
    miami_heat_21_22.to_csv('data/processed/miami_heat_games_21_22.csv', index=False)
    miami_heat_22_23.to_csv('data/processed/miami_heat_games_22_23.csv', index=False)
    west_conference.to_csv('data/processed/west_conference.csv', index=False)
    east_conference.to_csv('data/processed/east_conference.csv', index=False)
    bam_adebayo_profile.to_csv('data/processed/bam_adebayo_profile.csv', index=False)
    tyler_herro_profile.to_csv('data/processed/tyler_herro_profile.csv', index=False)
    jimmy_butler_profile.to_csv('data/processed/jimmy_butler_profile.csv', index=False)