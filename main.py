import json

class Ticket:
    def __init__(self, id, title, category, urgency, affected_users, priority, status):
        self.id = id
        self.title = title
        self.category = category
        self.urgency = urgency
        self.affected_users = affected_users
        self.priority = priority
        self.status = status
        self.assigned_to = None
    def display(self):
        print(f"Ticket ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Category: {self.category}")
        print(f"Urgency: {self.urgency}")
        print(f"Affected Users: {self.affected_users}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print(f"Assigned To: {self.assigned_to}")

class CampusFlow:
    def __init__(self):
        self.ticket_counter = 1
        self.tickets = []

    def id_generator(self):
        ticket_id = f'T{self.ticket_counter:03d}'
        self.ticket_counter += 1
        return ticket_id
    def priority_level(self, urgency, affected_users):
        if urgency == "high" and affected_users >= 10:
            return  "critical"
        elif urgency == "high" or affected_users >= 10:
            return "high"
        elif urgency == "medium" and affected_users >= 3:
            return "medium"
        else:
         return "low"

    def create_ticket(self):
        
        title = input("Enter the title of the ticket: ").strip().lower()
        while not title.lower().strip():
            print("Title cannot be empty. Please enter a valid title.")
            title = input("Enter the title of the ticket: ").strip().lower()
        categories = ['Software', 'Hardware', 'Network', 'Other']
        category = input("Enter the category of the ticket (Software, Hardware, Network, Other): ").title().strip()
        while category not in categories:
            print("Invalid category. Please enter a valid category.")
            category = input("Enter the category of the ticket (Software, Hardware, Network, Other): ").title().strip()
        
        urgency_levels = ['low', 'medium', 'high']
        urgency = input("Enter the urgency level of the ticket (low, medium, high): ").strip().lower()
        while urgency not in urgency_levels:
            print(f"Invalid urgency level. Please choose from {urgency_levels}.")
            urgency = input("Enter the urgency level of the ticket (low, medium, high): ").strip().lower()
        trial = 5
        while trial > 0:
                try: 
                    affected_users = int(input("Enter the number of affected users: ").strip())
                    if affected_users > 0:
                        break
                    elif affected_users < 0:
                        print("Number of affected users cannot be negative. Please enter a valid number.")
                        trial -= 1
                    else:
                        print("Number of affected users cannot be zero. Please enter a valid number.")
                        trial -= 1
                except ValueError:
                  print("Invalid input. Please enter a valid number.")
                  trial -= 1
                 
                
        if trial == 0:
            print("Too many invalid attempts. Ticket creation canceled.")
            return None

        priority = self.priority_level(urgency, affected_users)
    
        status = "Open"
        
        ticket_id = self.id_generator()
        ticket = Ticket(ticket_id, title, category, urgency, affected_users, priority, status)
        self.tickets.append(ticket)
        print(f"Ticket {ticket_id} created successfully with priority '{priority}' and status '{status}'.")
        return ticket
    
    def view_tickets(self):
        if not self.tickets:
            print("No tickets available.")
            return
        for ticket in self.tickets:
            ticket.display()
            print("-" * 20)

    def search_tickets(self,ticket_id):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                ticket.display()
                return
        print(f'{ticket_id} not found')

    def close_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                if ticket.status == "Closed":
                    print(f"{ticket_id} has been closed")
                else:
                    ticket.status = "Closed"
                    print(f"{ticket_id} has been closed")
                return
        print(f'{ticket_id} Ticket not Found!')

    def assign_ticket(self, ticket_id, staff_name):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                if ticket.status == "Closed":
                    print("Cannot assign a closed ticket.")
                    return

                ticket.assigned_to = staff_name
                print(f"Ticket {ticket_id} assigned to {staff_name}.")
                return

        print(f"Ticket {ticket_id} not found.")

    def save_tickets(self):
        ticket_data = []
        for ticket in self.tickets:
            ticket_data.append({
                "id": ticket.id,
                "title": ticket.title,
                "category":
                ticket.category,
                "urgency": ticket.urgency,
                "affected_users":ticket.affected_users,
                "priority":ticket.priority,
                "status": ticket.status,
                "assign_to":ticket.assigned_to

            })

            with open("tickets.json","w") as file:
                json.dump(ticket_data,file,indent="4")

    
    def load_tickets(self):
        try:
            with open("tickets.json", "r") as file:
                ticket_data = json.load(file)

            self.tickets = []

            for data in ticket_data:
                ticket = Ticket(
                    data["id"],
                    data["title"],
                    data["category"],
                    data["urgency"],
                    data["affected_users"],
                    data["priority"],
                    data["status"]
                )
                ticket.assigned_to = data["assigned_to"]
                self.tickets.append(ticket)

            print("Tickets loaded successfully.")

        except FileNotFoundError:
            print("No saved tickets file found.")

        self.ticket_counter = max(
        (int(ticket.id[1:]) for ticket in self.tickets),
        default=0) + 1






campus = CampusFlow()
campus.create_ticket()
campus.create_ticket()

campus.assign_ticket("T001","john")
campus.assign_ticket("T002","greydev")

campus.save_tickets()

                                
