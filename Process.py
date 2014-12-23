# -*- coding: utf-8 -*-


class Process:

	def __init__(self):
		pass

	#===========================================================================
    def startTaskDueDate(self):
        try:
            print(('run due date at ' + str(datetime.now())))
            overdueProcess = OverdueProcess()
            overdueProcess.startTaskDueDate()
        except:
            raise

    #===========================================================================
    def startTaskOverdue(self):
        try:
            print(('run scheduler at ' + str(datetime.now())))
            overdueProcess = OverdueProcess()
            overdueProcess.startTaskOverdue()
        except:
            raise	