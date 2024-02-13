import yaml
from sqlalchemy import create_engine as eng
from sqlalchemy import URL

class DatabaseConnector:
    def __init__(self):
        pass

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as file:
            database_creds = yaml.safe_load(file)
            return database_creds

    def init_db_engine(self):
        credentials = self.read_db_creds()
        url_object = URL.create(
            "postgresql",
            username=credentials['RDS_USER'],
            password=credentials['RDS_PASSWORD'], 
            host=credentials['RDS_HOST']
            database=credentials['RDS_DATABASE'],
            )
        engine = eng.create_engine(url_object)
        return engine