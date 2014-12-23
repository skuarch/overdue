# -*- coding: utf-8 -*-
from Connection import Connection
from datetime import date, timedelta, datetime, time
import os
import math
from TicketModel import TicketModel
from Utilities import Utilities


class OverdueProcess:

    #===========================================================================
    def __init__(self):        
        self.ticketModel = TicketModel()
        self.util = Utilities()

    #===========================================================================
    def startTaskOverdue(self):
        try:
            #get tickets from database
            tuples = self.ticketModel.getTuplesOverdue()                    
            if(len(tuples) > 0):

                for tuple in tuples:
                    ticket = self.util.createTicketFromTuple(tuple)                
                    if(datetime.now() >= ticket['dueDate']):
                        self.ticketModel.markTicketAsOverdue(ticket)
                        print('ticket ' + str(ticket['ticketId']) + ' is overdue')
                        
        except:
            raise
"""
    #===========================================================================
    def getTickets(self):
        sql = 'select * from Ticket where TicketStatus_ID in (1 , 2, 4, 5) and (TicketType_ID in (1 , 2, 3, 4, 5)) and (createTimeStamp >= SUBDATE(NOW(), 150) and createTimeStamp <= now() - interval 1 day) and (isOverdue = 0) order by createTimeStamp asc;';
        tickets = self.connection.executeStatement(sql)
        return tickets

    #===========================================================================
    def createTicketFromTuple(self, tupla):
        ticket = {"ticketId":tupla[0], "ticketType":tupla[1], "ticketStatus":tupla[2], "ticketSubmitterId":tupla[5], "severity":tupla[6], "isOverdue":tupla[11], "creationDate":tupla[14], "weekday":tupla[14].weekday()}
        return ticket

    #===========================================================================
    def ticketWasCreatedOnWeekend(self, ticket):
        #Monday is 0 and Sunday is 6
        if(ticket['weekday'] == 5 or ticket['weekday'] == 6):
            return True
        else:
            return False

    #===========================================================================
    def getBusinessDay(self, ticket):

        #0 monday, 1 tuesday, 2 wednesday, 3 thursday, 4 friday, 5 saturday, 6 sunday
        dateBusiness = ticket['creationDate']
        wasCreatedOnWeekend = self.ticketWasCreatedOnWeekend(ticket)

        if(wasCreatedOnWeekend):

            #ticket was created on saturday
            if(ticket['weekday'] == 5):

                if(ticket['severity'] == 2 or ticket['severity'] == 3):
                    d = ticket['creationDate'] + timedelta(days=2)
                    dateBusiness = d.strftime("%Y-%m-%d 00:00:00")

            #ticket was created on sunday
            if(ticket['weekday'] == 6):

                if(ticket['severity'] == 2 or ticket['severity'] == 3):
                    d = ticket['creationDate'] + timedelta(days=1)
                    dateBusiness = d.strftime("%Y-%m-%d 00:00:00")
        else:

            # monday and tuesday
            if(ticket['weekday'] == 0 or ticket['weekday'] == 1):
                dateBusiness = ticket['creationDate']

            #ticket created during the week
            if(ticket['severity'] == 2):
                #thursday and friday
                if(ticket['weekday'] == 3 or ticket['weekday'] == 4):
                    dateBusiness = ticket['creationDate'] + timedelta(days=2)

            if(ticket['severity'] == 3):

                #wendsday, thursday and friday
                if(ticket['weekday'] == 2 or ticket['weekday'] == 3 or ticket['weekday'] == 4):
                    dateBusiness = ticket['creationDate'] + timedelta(days=2)

        return dateBusiness

    #===========================================================================
    def markTicketAsOverdue(self, ticket):
        sql = 'update Ticket set isOverdue = 1 where Ticket_ID = '+ str(ticket['ticketId'])
        self.connection.executeUpdate(sql)

    #===========================================================================
    def insertRowSchedulerOverdueLog(self, ticketsUpdated, ticketToUpdate, processId, startDate):
        sql = 'insert into schedulerOverdueLog(start_date, end_date, tickets_to_update, tickets_updated, process_id) values ("' + str(startDate) + '", "' + str(datetime.now()) + '", '+str(ticketToUpdate) + ', ' + str(ticketsUpdated) + ', ' + str(processId) + ' )'
        insertId = self.connection.executeInsert(sql)
        return insertId

    #===========================================================================
    def insertIntoDebugScheduler(self, schedulerId, hourDifferences, ticket, datePlusDays):
        sql = 'INSERT INTO debugScheduler (scheduler_overdue_log_id,Ticket_ID,ticket_creation,date_current,Ticket_dayOfWeek,TicketDateCreation_plus_days,hourDifferences,severity,TicketType_ID)VALUES("' + str(schedulerId) +'", ' + str(ticket['ticketId']) + ' ,"' + str(ticket['creationDate']) + '","' + str(datetime.now()) + '",' + str(ticket['weekday']) + ',"' + str(datePlusDays) + '", '+ str(hourDifferences) +' ,'+ str(ticket['severity']) +',' + str(ticket['ticketId']) + ');'        
        self.connection.executeInsert(sql)

    #===========================================================================
    def updateSchedulerOverdueLog(self, schedulerId, ticketsUpdated):
        sql = 'update schedulerOverdueLog set tickets_updated = ' + str(ticketsUpdated) + ' where scheduler_overdue_log_id = ' + str(schedulerId) + ''        
        self.connection.executeUpdate(sql)
"""