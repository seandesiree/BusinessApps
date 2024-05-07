service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def new_ticket():
    while True:
        ticket_id = "Ticket{:03d}".format(len(service_tickets) + 1)
        service_tickets[ticket_id] = {}
        service_tickets[ticket_id]["Customer"] = input("What is your name? ")
        service_tickets[ticket_id]["Issue"] = input("What is the issue? ")
        service_tickets[ticket_id]["Status"] = "open"
        print(f"A new ticket with unique ID: '{ticket_id}' has been added. ")

        another_ticket = input("Do you want to add another ticket? ")
        if another_ticket.lower() != 'yes':
            break

          
def update_status():
    ticket_id = input("What is the ticket ID number? ")
    status_update = input("Is the status 'open' or 'closed'? ")
    service_tickets[ticket_id]["Status"] = (status_update)
    print(f"The state for {ticket_id} has been updated to {status_update} ")


def display_tickets(service_tickets):
    filter_status = input("Would you like to filter tickets by status? Type 'open' or 'closed' to filter (press Enter to display all tickets): ").lower()
    
    for ticket_id, ticket_info in service_tickets.items():
        if not filter_status or ticket_info["Status"].lower() == filter_status:
            print(f"{ticket_id}: Customer - {ticket_info['Customer']}, Issue - {ticket_info['Issue']}, Status - {ticket_info['Status']}")

