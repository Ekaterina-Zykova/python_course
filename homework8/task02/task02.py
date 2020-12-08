import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def _cursor(self):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return cursor

    def _names_column(self):
        sql_query = "SELECT * FROM " + self.table_name
        cursor = self._cursor().execute(sql_query)
        names_column = list(map(lambda x: x[0], cursor.description))
        return names_column

    def __len__(self):
        sql_query = "SELECT * FROM " + self.table_name
        cursor = self._cursor().execute(sql_query)
        return len(cursor.fetchall())

    def __getitem__(self, key: str):
        sql_query = "SELECT * FROM " + self.table_name + " WHERE "
        for name in self._names_column():
            sql_for_res = sql_query + name + "=?"
            cursor = self._cursor().execute(sql_for_res, (key,))
            result = cursor.fetchall()
            if result:
                return result

    def __contains__(self, item: str):
        sql_query = "SELECT * FROM " + self.table_name + " WHERE "
        for name in self._names_column():
            sql_for_res = sql_query + name + "=?"
            cursor = self._cursor().execute(sql_for_res, (item,))
            result = cursor.fetchall()
            if result:
                return item

    def __iter__(self):
        result = dict()
        sql_query = "SELECT * FROM " + self.table_name
        for row in self._cursor().execute(sql_query):
            for i, name in enumerate(self._names_column()):
                result[name] = row[i]
            yield result
