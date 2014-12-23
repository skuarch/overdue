-- --------------------------------------------------------------------------------
-- Routine DDL
-- Note: comments before and after the routine body will not be stored by the server
-- --------------------------------------------------------------------------------
DELIMITER $$

CREATE DEFINER=`root`@`localhost` FUNCTION `calculateDueDate`(p_Ticket_ID bigint) RETURNS datetime
    DETERMINISTIC
BEGIN
    DECLARE dueDate datetime;
    set @log_id = 0;
    set @tickets_to_update = 0;
    set @updates_num = 0;        
    set @ticket_severity = 0;
    set @ticket_real_creation = "";
    set @ticket_creation = "";
    set @ticket_status = 0;     
    set @difference = 0;        
    set @ticket_type = 0;
    set @dayweek = 0;
    set @total_rows = 0;
    set @ticket_creation_hour = 0;
    set @diff_creation_hour = 0;

    select createTimeStamp, severity, TicketType_ID, TicketStatus_ID into @ticket_creation, @ticket_severity, @ticket_type, @ticket_status from Ticket where Ticket_ID = p_Ticket_ID;
    set @ticket_real_creation = @ticket_creation;

    

    
    if @ticket_type = 6 then 

        RETURN null;

    end if;

    
    if @ticket_type = 0 then 
        
        RETURN null;

    end if;

    

    #5 = thriedat
    #1 = Sunday, 2 = Monday, …, 7 = Saturday
    
    set @dayweek = dayofweek(@ticket_creation);             

    
    if @dayweek = 7 then
        
        if @ticket_severity = 2 or @ticket_severity = 3 then
            
            set @next_busines_day = concat(year(@ticket_creation), '-',month(@ticket_creation),'-', day(@ticket_creation), ' 00:00:00');
            set @next_busines_day = date_add(@next_busines_day, interval 2 day);                    
            set @ticket_creation = cast(@next_busines_day as char); 

        end if;

    end if;

    
    if @dayweek = 1 then
        
        if @ticket_severity = 2 or @ticket_severity = 3 then    
            
            set @next_busines_day = concat(year(@ticket_creation), '-',month(@ticket_creation),'-', day(@ticket_creation), ' 00:00:00');
            set @next_busines_day = date_add(@next_busines_day, interval 1 day);                    
            set @ticket_creation = cast(@next_busines_day as char); 
        end if;

    end if; 

    
    
    
    if @ticket_severity = 2 then    

        set @dayweek = dayofweek(@ticket_creation);             

        if  @dayweek = 5 then 
            set @ticket_creation = adddate(@ticket_creation,2);
        end if;

        if  @dayweek = 6 then 
            set @ticket_creation = adddate(@ticket_creation,2);
        end if;             

    end if;

    
    if @ticket_severity = 3 then    

        set @dayweek = dayofweek(@ticket_creation);             

        if  @dayweek = 4 then 
            set @ticket_creation = adddate(@ticket_creation,2);
        end if;

        if  @dayweek = 5 then 
            set @ticket_creation = adddate(@ticket_creation,2);
        end if;

        if  @dayweek = 6 then 
            set @ticket_creation = adddate(@ticket_creation,2);
        end if;
        
    end if;


    


    if @ticket_severity = 1 then

        SET dueDate = adddate(@ticket_creation, 1);

    end if;


    if @ticket_severity = 2 then

        SET dueDate = adddate(@ticket_creation, 2);

    end if;


    if @ticket_severity = 3 then

        SET dueDate = adddate(@ticket_creation, 3);

    end if;

    RETURN dueDate;
END