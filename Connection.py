# -*- coding: utf-8 -*-
from MysqlConnection import MysqlConnection
import config


class Connection:

    #===========================================================================
    def __init__(self):
        pass

    #===========================================================================
    #execute select sentence
    def executeStatement(self, query):
        connection = None
        try:
            connection = MysqlConnection(
                config.dbHost,
                config.dbUser,
                config.dbPassword,
                config.dbName,
                config.dbPort)
            connection.openConnection()
            connection.createCursor()
            connection.executeStatement(query)
            return connection.getResults()
        except:
            raise
        finally:
            self.closeConnection(connection)

    #===========================================================================
    #execute insert,drop or update sentence
    def executeUpdate(self, query):
        connection = None
        idInsert = 0
        try:
            connection = MysqlConnection(
                    config.dbHost,
                    config.dbUser,
                    config.dbPassword,
                    config.dbName,
                    config.dbPort)
            connection.openConnection()
            connection.createCursor()
            connection.executeStatement(query)            
            connection.executeCommit()            
        except:
            raise
        finally:
            self.closeConnection(connection)

    #===========================================================================
    #execute insert
    def executeInsert(self, query):
        connection = None
        idInsert = 0
        try:
            connection = MysqlConnection(
                    config.dbHost,
                    config.dbUser,
                    config.dbPassword,
                    config.dbName,
                    config.dbPort)
            connection.openConnection()
            connection.createCursor()
            connection.executeStatement(query)
            idInsert = connection.getIdInsert()
            connection.executeCommit()
            return idInsert
        except:
            raise
        finally:
            self.closeConnection(connection)
            
    #===========================================================================
    def closeConnection(self, connection):
        try:
            connection.closeCursor()
            connection.closeConnection()
        except:
            raise