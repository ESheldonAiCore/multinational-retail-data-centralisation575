#%%

from database_utils import DatabaseConnector

if __name__ == '__main__':
    database_connection = DatabaseConnector()
    database_connection.read_db_creds()
#%%
