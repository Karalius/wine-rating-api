import psycopg2
import os
from typing import Union, Dict, Any


class Database:
    """
    This class connects to Heroku hosted Postgres database.

    Methods:
    -------------------------------------------------------------
    *create_table: create a table in Postgres

    *get_last_ten_inferences: returns 10 last rows in the database

    *insert: inserts model's input and ouput in json format

    *drop_table: drops the table in the database
    -------------------------------------------------------------
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def connect() -> Union[None, str]:
        try:
            connection = psycopg2.connect(os.environ["DATABASE_URL"])
            connection.autocommit = True
            cur = connection.cursor()
            return cur
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_table(self) -> None:
        with self.connect() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS inferences (
                    id serial PRIMARY KEY,
                    input json NOT NULL,
                    output json NOT NULL
                    );"""
            )

    def get_last_ten_inferences(self) -> list:
        with self.connect() as cur:
            cur.execute(
                """
                SELECT *
                FROM inferences
                ORDER BY id DESC
                LIMIT 10;"""
            )
            rows = cur.fetchall()
        return rows

    def insert(self, input: Dict[str, Any], output: Dict[str, Any]) -> Union[None, str]:
        try:
            with self.connect() as cur:
                cur.execute(
                    f"INSERT INTO inferences(input, output)"
                    f"VALUES ('{input}', '{output}');"
                )
        except SyntaxError as error:
            print(f"Invalid syntax within JSON {error}")

    def drop_table(self) -> None:
        with self.connect() as cur:
            cur.execute(
                """
                DROP TABLE IF EXISTS
                inferences;"""
            )
