class Ticket:
  def __init__(self, ticket_id, title, priority):
    self.ticket_id = ticket_id
    self.title = title
    self.priority = priority
    self.status = "Open"

  def close_ticket(self):
    self.status = "Closed"

  def __str__(self):
    return f"ID: {self.ticket_id} | Title: {self.title} | Priority: {self.priority} | Status: {self.status}"


class HelpDesk:
  def __init__(self):
    self.tickets = []
    self.next_id = 1

  def create_ticket(self, title, priority):
    ticket = Ticket(self.next_id, title, priority)
    self.tickets.append(ticket)
    self.next_id += 1
    print("Ticket created successfully.")

  def view_tickets(self):
    if not self.tickets:
    print("No tickets found.")
    for ticket in self.tickets:
    print(ticket)

  def close_ticket(self, ticket_id):
    for ticket in self.tickets:
      if ticket.ticket_id == ticket_id:
      ticket.close_ticket()
      print("Ticket closed successfully.")
      return
    print("Ticket not found.")


def main():
  helpdesk = HelpDesk()

  while True:
    print("\n--- IT Help Desk System ---")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Close Ticket")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
      title = input("Enter issue title: ")
      priority = input("Enter priority (Low/Medium/High): ")
      helpdesk.create_ticket(title, priority)

    elif choice == "2":
      helpdesk.view_tickets()

    elif choice == "3":
      ticket_id = int(input("Enter ticket ID to close: "))
      helpdesk.close_ticket(ticket_id)

    elif choice == "4":
      break

    else:
      print("Invalid option.")


if __name__ == "__main__":
    main()
