# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime, time
from Utilities import Utilities
from TicketModel import TicketModel


class DueDateProcess:

	#===========================================================================
    def __init__(self):
    	self.ticketModel = TicketModel()
    	self.util = Utilities()

    #===========================================================================	
    def startTaskDueDate(self):

        try:
            #get tickets from database            
            tuples = self.ticketModel.getTuplesDueDateNull()                    
            if(len(tuples) > 0):

                for tuple in tuples:
                    ticket = self.util.createTicketFromTuple(tuple)                
                    dd = self.util.getDueDate(ticket['creationDate'], ticket['severity'])                                        
                    self.ticketModel.updateTicketDueDate(ticket['ticketId'], dd)
                    print('ticket date: ' + str(ticket['creationDate']) + ' dueDate: ' + str(dd) + ' severity: ' + str(ticket['severity']))          
        except:
            raise