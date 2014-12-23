# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime, time


class Utilities:

    #===========================================================================
    def __init__(self):
        pass

    #===========================================================================
    def formatDate(self, date):
        try:
            if (date is not None):
                return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            else:
                raise Exception("illegal arguments")
        except:
            raise        

    #===========================================================================
    def createTicketFromTuple(self, tuple):
        try:
            ticket = {"ticketId":tuple[0], "ticketType":tuple[1], "ticketStatus":tuple[2], "ticketSubmitterId":tuple[5], "severity":tuple[6], "isOverdue":tuple[11], "creationDate":tuple[14], "weekday":tuple[14].weekday(), "dueDate":tuple[22] }
            return ticket
        except:
            raise    	

    #===========================================================================
    def getDueDate(self, creationDate, severity):
        
        try:
            #0 monday, 1 tuesday, 2 wednesday, 3 thursday, 4 friday, 5 saturday, 6 sunday        
            weekday = creationDate.weekday()
            print(weekday)
            dueDate = None
            sev = int(severity)

            #saturday
            if (weekday == 5):
                if (sev == 2 or sev == 3):
                    creationDate = creationDate + timedelta(days=2)                
                    nd = str(creationDate.year) + '-' + str(creationDate.month) + '-' + str(creationDate.day) + ' 00:00:00' 
                    creationDate = self.formatDate(nd)
            #sunday        
            if (weekday == 6):
                if (sev == 2 or sev == 3):
                    creationDate = creationDate + timedelta(days=1)
                    nd = str(creationDate.year) + '-' + str(creationDate.month) + '-' + str(creationDate.day) + ' 00:00:00' 
                    creationDate = self.formatDate(nd)

            if (sev == 2):
                weekday = creationDate.weekday()

                #thursday and friday
                if (weekday == 3 or weekday == 4):
                    creationDate = creationDate + timedelta(days=2)         

            if (sev == 3):
                weekday = creationDate.weekday()

                #wednesday, thursday and friday
                if (weekday == 2 or weekday == 3 or weekday == 4):
                    creationDate = creationDate + timedelta(days=2) 

            #===========================================================================
            if (sev == 1):
                dueDate = creationDate + timedelta(days=1)                 

            if (sev == 2):
                dueDate = creationDate + timedelta(days=2)

            if (sev == 3):
                dueDate = creationDate + timedelta(days=3)

            return dueDate
        except:
            raise        