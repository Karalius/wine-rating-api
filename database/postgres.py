import psycopg2
import os
from typing import Union, Dict, Any


class Database:

    def __init__(self) -> None:
        pass


    @staticmethod
    def connect() -> Union[None, str]:
        try:
            connection = psycopg2.connect(os.environ['DATABASE_URL'])
            connection.autocommit = True
            cur = connection.cursor()
            return cur
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def create_table(self) -> None:
        cur = self.connect()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS inferences (
                id serial PRIMARY KEY,
                input json NOT NULL,
                output json NOT NULL
                );"""
                )
        cur.close()


    def get_last_ten_inferences(self) -> list:
        cur = self.connect()
        cur.execute(
            """
            SELECT *
            FROM inferences
            ORDER BY id DESC
            LIMIT 10;"""
            )
        rows = cur.fetchall()
        cur.close()
        return rows
    

    def insert(self, input: Dict[str, Any], output: Dict[str, Any]) -> Union[None, str]:
        try:
            cur = self.connect()
            cur.execute(
                f"INSERT INTO inferences(input, output)"
                f"VALUES ('{input}', '{output}');"
                )
            cur.close()
        except SyntaxError as error:
            print(f'Invalid syntax within JSON {error}')

    
    def drop_table(self) -> None:
        cur = self.connect()
        cur.execute(
            """
            DROP TABLE IF EXISTS
            inferences;"""
            )
        cur.close()
