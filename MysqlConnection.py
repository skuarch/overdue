# -*- coding: utf-8 -*-
import MySQLdb
from MySQLdb import cursors


class MysqlConnection:

    #===========================================================================
    def __init__(self, hostname, user, password, database, port):
        self.hostname = hostname
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.db = None
        self.cursor = None
        self.query = None

    #===========================================================================
    def openConnection(self):
        try:
            if (self.hostname == None or len(self.hostname) < 1):
                raise Exception("illegal arguments hostname")
            if (self.user == None or len(self.user) < 1) :
                raise Exception("illegal arguments user")
            if(self.database == None or len(self.database) < 1):
                raise Exception("illegal arguments database")

            self.db = MySQLdb.connect(
                self.hostname,
                self.user,
                self.password,
                self.database,
                self.port,
                cursorclass=MySQLdb.cursors.SSCursor)
        except:
            raise

    #===========================================================================
    def createCursor(self):
        try:
            self.cursor = self.db.cursor(cursors.SSCursor)
        except:
            raise

    #===========================================================================
    def executeStatement(self, query):
        self.query = query
        try:
            if self.query is None or len(self.query) < 1:
                raise Exception("error", "query is null or empty")
            self.cursor.execute(self.query)            
        except:
            raise

    #===========================================================================
    def executeCommit(self):
        try:
            self.db.commit()
        except:
            raise

    #===========================================================================
    def rollback(self):
        try:
            self.db.rollback()
        except:
            raise

    #===========================================================================
    def getResults(self):
        try:
            return self.cursor.fetchall()
        except:
            raise        

    #===========================================================================
    def getColumns(self):
        try:
            return self.cursor.description
        except:
            raise

    #===========================================================================
    def getIdInsert(self):
        try:
            return self.db.insert_id()
        except:
            raise

    #===========================================================================
    def closeConnection(self):
        try:
            if(self.db is not None):
                self.db.close()
        except:
            raise

    #===========================================================================
    def closeCursor(self):
        try:
            if(self.cursor is not None):
                self.cursor.close()
        except:
            raise