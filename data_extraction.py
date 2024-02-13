class DataExtractor:
    def __init__(self):
        pass

    def list_db_tables(self,engine):
        list_tables = metadata.reflect(engine)
        return list_tables
