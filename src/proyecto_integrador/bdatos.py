import os
import sqlite3
import pandas as pd
from typing import Optional


class Bdatos:
    def __init__(self, db_path: str):
        self.db_path= db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
    
    def crear_tabla(self, sql_create: str) -> None:
        self.cursor.execute(sql_create)
        self.conn.commit()

    def insertar_dataframe(
        self,
        df:pd.DataFrame,
        tabla: str,
        if_exists: str = "append",
        index: bool = False
    ) ->None:
        
        df.to_sql(
            name=tabla,
            con=self.conn,
            if_exists=if_exists,
            index=index
        )

    def consultar(self, sql_query: str) -> pd.DataFrame:
        return pd.read_sql_query(sql_query, self.conn)

    def cerrar(self) -> None:
        self.conn.close()
