import os
import psycopg2
from dotenv import load_dotenv

load_dotenv();

PG_USER= os.getenv('PG_USER')
PG_PASSWORD=os.getenv('PG_PASSWORD')
PG_PORT=os.getenv('PG_PORT')
PG_DATABASE=os.getenv('PG_DATABASE')
PG_HOST=os.getenv('PG_HOST')

def get_db():
	conn = psycopg2.connect(database=PG_DATABASE, user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT)
	return conn


