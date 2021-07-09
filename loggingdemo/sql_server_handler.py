import logging
from logging import LogRecord
import pyodbc 


# https://docs.python.org/3/library/logging.html#logrecord-attributes

class SqlServerHandler(logging.Handler):

    def __init__(self, connection_string:str, table:str):
        """
        SqlServerHandler class constructor
        Parameters:
            self: instance of the class
            database: database
            table: log table name
            attributes_list: log table columns
        Returns:
            None
        """

        super().__init__()
        self._connection_string = connection_string
        self._table = table


    def emit(self, record: LogRecord) -> None:
        """
            Save the log record to SQL Server
            Parameters:
                self: instance of the class
                record: log record to be saved
            Returns:
                None
        """

        # Use configured formatter, sql is all driven of the config.
        sql = self.format(record).replace('{{table}}', self._table)

        conn = pyodbc.connect(self._connection_string)
        cursor = conn.cursor()

        # todo pass as parameters not pure sql, sql injection kills!
        count = cursor.execute(sql).rowcount
        conn.commit()