# -*- coding: utf-8 -*-
from Connection import Connection

class TicketModel:

	#===========================================================================
    def __init__(self):
        pass

	#===========================================================================
    def getTuplesDueDateNull(self):
        try:
            connection = Connection()
            sql = 'select * from Ticket where dueDateTimeStamp is null and TicketType_ID in (1, 2, 3, 4, 5);'
            tickets = connection.executeStatement(sql)
            return tickets
        except:
            raise        

    #===========================================================================
    def getTuplesOverdue(self):
        try:
            connection = Connection()
            sql = 'select * from Ticket where (isOverdue = 0) and (dueDateTimeStamp is not null) and (TicketStatus_ID in (1 , 2, 4, 5)) and ((TicketType_ID in (1 , 2, 3, 4, 5)));'
            tickets = connection.executeStatement(sql)
            return tickets
        except:
            raise        

	#===========================================================================	
    def updateTicketDueDate(self, ticketId, dueDate):
        try:
            connection = Connection()
            sql = 'update Ticket set dueDateTimeStamp = "' + str(dueDate) + '" where Ticket_ID = ' + str(ticketId)
            connection.executeUpdate(sql)
        except:
            raise        

    #===========================================================================
    def markTicketAsOverdue(self, ticket):
        try:
            connection = Connection()
            sql = 'update Ticket set isOverdue = 1 where Ticket_ID = ' + str(ticket['ticketId'])
            connection.executeUpdate(sql)
        except:
            raise      