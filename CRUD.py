import pandas as pd
import psycopg2  # allow to run commands against db
from sqlalchemy import create_engine
# sqlalchemy is needed to allow pandas to seemlessly connect to run queries


conn = psycopg2.connect("dbname=consumer_complaints user=playgrnd")
conn.autocommit = True
cur = conn.cursor()


def run_command(command):
    cur.execute(command)
    return cur.statusmessage


engine = create_engine('postgresql://playgrnd@localhost/consumer_complaints')


def run_query(query):
    return pd.read_sql_query(query, con=engine)
