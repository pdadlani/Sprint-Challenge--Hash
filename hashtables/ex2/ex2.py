#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    starting point has source of 'NONE'
    ending point has destination of 'NONE'

    every ith-1 ticket's destination is ith ticket's source

    connect this list of tickets where the result shows the path

    storing the given tickets in a dict will help for easy/quick access
    """

    ticket_dict = dict()

    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    route = []

    curr_city = ticket_dict['NONE']
    route.append(curr_city)

    while curr_city is not 'NONE':
        curr_city = ticket_dict[curr_city]
        route.append(curr_city)

    return route
