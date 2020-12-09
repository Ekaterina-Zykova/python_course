import sqlite3


class TableData:
    _sql_query = "SELECT * FROM "

    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name
        self._sql_query += table_name

    def _cursor(self):
        with sqlite3.connect(self.database_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            return cursor

    def __len__(self):
        cursor = self._cursor().execute(self._sql_query)
        length = len(cursor.fetchall())
        cursor.close()
        return length

    def __getitem__(self, key: str):
        cursor = self._cursor().execute(self._sql_query)
        names_column = cursor.fetchone().keys()
        for name in names_column:
            sql_for_res = self._sql_query + " WHERE " + name + "=?"
            cursor = self._cursor().execute(sql_for_res, (key,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return tuple(result)

    def __contains__(self, item: str):
        cursor = self._cursor().execute(self._sql_query)
        names_column = cursor.fetchone().keys()
        for name in names_column:
            sql_for_res = self._sql_query + " WHERE " + name + "=?"
            cursor = self._cursor().execute(sql_for_res, (item,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return result

    def __iter__(self):
        result = self._cursor().execute(self._sql_query)
        self._cursor().close()
        return result
