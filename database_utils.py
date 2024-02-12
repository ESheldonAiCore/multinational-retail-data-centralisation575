import yaml

class DatabaseConnector:
    def __init__(self):
        return self

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as file:
            database_creds = yaml.safe_load(file)
            print(database_creds)