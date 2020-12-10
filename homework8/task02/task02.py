import sqlite3


class TableData:
    _sql_query = "SELECT * FROM "

    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name
        self._sql_query += table_name

    def __enter__(self):
        self._conn = sqlite3.connect(self.database_name)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._conn.close()

    def __len__(self):
        sql_query = "SELECT COUNT(*) FROM " + self.table_name
        cursor = self._cursor.execute(sql_query)
        length = cursor.fetchone()[0]
        return length

    def __getitem__(self, key: str):
        cursor = self._cursor.execute(self._sql_query)
        names_column = cursor.fetchone().keys()
        for name in names_column:
            sql_for_res = self._sql_query + " WHERE " + name + "=?"
            cursor = self._cursor.execute(sql_for_res, (key,))
            result = cursor.fetchone()
            if result:
                return tuple(result)

    def __contains__(self, item: str):
        cursor = self._cursor.execute(self._sql_query)
        names_column = cursor.fetchone().keys()
        for name in names_column:
            sql_for_res = self._sql_query + " WHERE " + name + "=?"
            cursor = self._cursor.execute(sql_for_res, (item,))
            result = cursor.fetchone()
            if result:
                return result

    def __iter__(self):
        result = self._cursor.execute(self._sql_query)
        return result
