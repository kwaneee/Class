
#What headers should look like:
# def fn_name(param1: type,...) -> return_type:


price_per_ticket = 5
fixed_cost = 20
cost_per_attendee = 0.50


#STEP 2:
def total_profit (attendees: int) -> float:
    
    
    #STEP 1:
    #docstring must be indented 4 spaces
    """ Return the total profit of a thatres in a movie per attendee
    #STEP #:

    >>>total_profit(5)
    2.5
    """

    return price_per_ticket * attendees - ( fixed_cost + attendees * cost_per_attendee)



