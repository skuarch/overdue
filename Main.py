# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from Connection import Connection
import time
import config
from OverdueProcess import OverdueProcess
from DueDateProcess import DueDateProcess
import os
import threading


class Main:

    #===========================================================================
    def __init__(self):
        self.logger = None
        self.connection = Connection()
        self.isRunningWorkerDueDate = False
        self.isRunningWorkerOverdueDate = False
        print(("starting program process:" + str(os.getpid())))
        self.configureLoggin()

        while True:
            try:                
                self.startTaskDueDate()
                self.startTaskOverdue()
            except Exception as e:                
                self.logger.exception(e)
                print(e)
            
            time.sleep(config.taskSleep)

        self.logger.info('program ends')

    #===========================================================================
    def configureLoggin(self):
        print('configuring logging')
        self.logger = logging.getLogger(config.logName)
        self.logger.setLevel(config.logLevel)
        logHandler = logging.FileHandler(config.logFileName)
        logHandler.setLevel(config.logLevel)
        formatter = logging.Formatter(config.logFormat)
        logHandler.setFormatter(formatter)
        self.logger.addHandler(logHandler)

    #===========================================================================
    def startTaskDueDate(self):
        try:
            if(self.isRunningWorkerDueDate == False):           
                print(('run due date scheduler at ' + str(datetime.now())))
                t = threading.Thread(target=self.workerDueDate)
                t.start()
        except:            
            raise

    #===========================================================================
    def startTaskOverdue(self):
        try:
            if(self.isRunningWorkerOverdueDate == False):
                print(('run overdue scheduler at ' + str(datetime.now())))
                t = threading.Thread(target=self.workerOverdue)
                t.start()
        except:            
            raise

    #===========================================================================
    def workerDueDate(self): 
        try:
            self.isRunningWorkerDueDate = True
            dueDateProcess = DueDateProcess()
            dueDateProcess.startTaskDueDate()
            self.isRunningWorkerDueDate = False
        except:
            self.isRunningWorkerDueDate = False
            raise        

    #===========================================================================
    def workerOverdue(self):   
        try:
            self.isRunningWorkerOverdueDate = True
            overdueProcess = OverdueProcess()
            overdueProcess.startTaskOverdue()
            self.isRunningWorkerOverdueDate = False
        except:
            self.isRunningWorkerOverdueDate = False
            raise

main = Main()