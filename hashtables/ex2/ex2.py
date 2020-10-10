from hashtable import HashTable

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    hashtable = HashTable(length);
    route = [None] * length;

    for ticket in tickets:
        hashtable.put(ticket.source, ticket.destination)

    # first route
    route[0] = hashtable.get("NONE")

    # get previous ticket, knowing destination
    for i in range(1, length):
        route[i] = hashtable.get(route[i-1])

    return route
