import pandas as pd
import sqlalchemy

"""
Loads mediascan.db
"""


def load_db(db_path: str = "sqlite:///../../out/mediascan.db"):
    engine = sqlalchemy.create_engine(db_path)
    return engine


def get_df_artists(engine: sqlalchemy.Engine):
    with engine.connect() as conn:
        artists = pd.read_sql_query("SELECT * FROM artist", conn)
        return artists


def get_df_files_artistdata_joined(engine: sqlalchemy.Engine):
    with engine.connect() as conn:
        files = pd.read_sql_query(
            "SELECT * FROM mediafile LEFT JOIN artist ON mediafile.artistpath = artist.path", conn
        )
        return files
