from datetime import datetime
from typing import List, Any
import tkinter as tk
from tkinter import messagebox
import pickle

class Employee:
    """Represents an employee with various personal and professional details."""

    def __init__(self, name: str, employeeID: str, department: str, jobTitle: str, basicSalary: float, age: int,
                 dateOfBirth: str, passportDetails: str):
        """Initialize an employee with provided attributes."""
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = datetime.strptime(dateOfBirth, '%Y-%m-%d')
        self.passportDetails = passportDetails

    def manage_employee(self) -> str:
        """Simulate managing subordinate employees."""
        return f"Managing Employees under {self.name}"


class Client:
    """Represents a client who organizes events."""

    def __init__(self, clientID: str, name: str, address: str, contactDetails: str, budget: float):
        """Initialize a client with specified details."""
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

    def update_client_info(self) -> str:
        """Update information for the client."""
        return f"Updated client info for {self.name}"


class Guest:
    """Represents a guest attending an event."""

    def __init__(self, guestID: str, name: str, address: str, contactDetails: str):
        """Initialize a guest with specified details."""
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    def update_guest_info(self) -> str:
        """Update information for the guest."""
        return f"Updated guest info for {self.name}"


class Event:
    """Represents an event managed by the company."""

    def __init__(self, eventID: str, type: str, theme: str, date: str, time: str, duration: float, venueAddress: str,
                 client: Client, guests: List[Guest], suppliers: List[Any], invoice: str):
        """Initialize an event with all necessary details and associations."""
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.client = client
        self.guests = guests
        self.suppliers = suppliers
        self.invoice = invoice

    def schedule_event(self) -> str:
        """Schedule the event according to given details."""
        return f"Event {self.type} scheduled on {self.date}"

    def update_event_details(self) -> str:
        """Update the details of the event."""
        return f"Updated event details for {self.eventID}"


class Supplier:
    """Abstract base class for suppliers providing various services for events."""

    def __init__(self, supplierID: str, name: str, address: str, contactDetails: str):
        """Initialize a supplier with common details."""
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    def update_supplier_info(self) -> str:
        """Update information for the supplier."""
        return f"Updated supplier info for {self.name}"


class Venue:
    """Represents a venue where events are held."""

    def __init__(self, venueID: str, name: str, address: str, contact: str, minGuests: int, maxGuests: int):
        """Initialize a venue with capacity details and location."""
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def update_venue_info(self) -> str:
        """Update details about the venue."""
        return f"Venue updated: {self.name}"


# Derived Supplier classes
class Caterer(Supplier):
    """Specific supplier type for catering services at events."""

    def __init__(self, supplierID: str, name: str, address: str, contactDetails: str, menu: str, minGuests: int,
                 maxGuests: int):
        """Initialize a caterer with menu and guest capacity details."""
        super().__init__(supplierID, name, address, contactDetails)
        self.menu = menu
        self.minGuests = minGuests
        self.maxGuests = maxGuests


class Decorator(Supplier):
    """Specific supplier type for decoration services at events."""
    # Additional attributes or methods specific to decorators can be added here.

class Cleaner(Supplier):
    """Specific supplier type for cleaning services at events."""
    # Additional attributes or methods specific to cleaners can be added here.

class Entertainer(Supplier):
    """Specific supplier type for entertainment services at events."""
    # Additional attributes or methods specific to entertainers can be added here.

class FurnitureSupplier(Supplier):
    """Specific supplier type for supplying furniture at events."""
    # Additional attributes or methods specific to furniture suppliers can be added here.

def merge_codes():
    class EventManagementApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Event Management System")

            # Load existing data from binary files
            self.load_data()

            # Create buttons to perform actions
            self.employee_button = tk.Button(root, text="Manage Employees", command=self.manage_employees)
            self.employee_button.pack()

            self.event_button = tk.Button(root, text="Manage Events", command=self.manage_events)
            self.event_button.pack()

            self.client_button = tk.Button(root, text="Manage Clients", command=self.manage_clients)
            self.client_button.pack()

            self.guest_button = tk.Button(root, text="Manage Guests", command=self.manage_guests)
            self.guest_button.pack()

            self.supplier_button = tk.Button(root, text="Manage Suppliers", command=self.manage_suppliers)
            self.supplier_button.pack()

            self.venue_button = tk.Button(root, text="Manage Venues", command=self.manage_venues)
            self.venue_button.pack()

        def load_data(self):
            try:
                with open('employees.pkl', 'rb') as f:
                    self.employees = pickle.load(f)
            except FileNotFoundError:
                self.employees = {}

            try:
                with open('events.pkl', 'rb') as f:
                    self.events = pickle.load(f)
            except FileNotFoundError:
                self.events = {}

            try:
                with open('clients.pkl', 'rb') as f:
                    self.clients = pickle.load(f)
            except FileNotFoundError:
                self.clients = {}

            try:
                with open('guests.pkl', 'rb') as f:
                    self.guests = pickle.load(f)
            except FileNotFoundError:
                self.guests = {}

            try:
                with open('suppliers.pkl', 'rb') as f:
                    self.suppliers = pickle.load(f)
            except FileNotFoundError:
                self.suppliers = {}

            try:
                with open('venues.pkl', 'rb') as f:
                    self.venues = pickle.load(f)
            except FileNotFoundError:
                self.venues = {}

        def save_data(self):
            with open('employees.pkl', 'wb') as f:
                pickle.dump(self.employees, f)

            with open('events.pkl', 'wb') as f:
                pickle.dump(self.events, f)

            with open('clients.pkl', 'wb') as f:
                pickle.dump(self.clients, f)

            with open('guests.pkl', 'wb') as f:
                pickle.dump(self.guests, f)

            with open('suppliers.pkl', 'wb') as f:
                pickle.dump(self.suppliers, f)

            with open('venues.pkl', 'wb') as f:
                pickle.dump(self.venues, f)

        def manage_employees(self):
            employee_window = tk.Toplevel(self.root)
            employee_window.title("Manage Employees")

            tk.Label(employee_window, text="Employee ID:").grid(row=0, column=0)
            employee_id_entry = tk.Entry(employee_window)
            employee_id_entry.grid(row=0, column=1)

            tk.Label(employee_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(employee_window)
            name_entry.grid(row=1, column=1)

            add_button = tk.Button(employee_window, text="Add Employee", command=lambda: self.add_employee(employee_id_entry.get(), name_entry.get()))
            add_button.grid(row=2, column=0)

            delete_button = tk.Button(employee_window, text="Delete Employee", command=lambda: self.delete_employee(employee_id_entry.get()))
            delete_button.grid(row=2, column=1)

            display_button = tk.Button(employee_window, text="Display Employee", command=lambda: self.display_employee(employee_id_entry.get()))
            display_button.grid(row=2, column=2)

        def add_employee(self, emp_id, name):
            if emp_id in self.employees:
                messagebox.showerror("Error", "Employee with ID already exists.")
            else:
                self.employees[emp_id] = name
                self.save_data()
                messagebox.showinfo("Success", "Employee added successfully.")

        def delete_employee(self, emp_id):
            if emp_id in self.employees:
                del self.employees[emp_id]
                self.save_data()
                messagebox.showinfo("Success", "Employee deleted successfully.")
            else:
                messagebox.showerror("Error", "Employee not found.")

        def display_employee(self, emp_id):
            if emp_id in self.employees:
                messagebox.showinfo("Employee Details", f"Employee ID: {emp_id}\nName: {self.employees[emp_id]}")
            else:
                messagebox.showerror("Error", "Employee not found.")

        def manage_events(self):
            event_window = tk.Toplevel(self.root)
            event_window.title("Manage Events")

            tk.Label(event_window, text="Event ID:").grid(row=0, column=0)
            event_id_entry = tk.Entry(event_window)
            event_id_entry.grid(row=0, column=1)

            tk.Label(event_window, text="Type:").grid(row=1, column=0)
            type_entry = tk.Entry(event_window)
            type_entry.grid(row=1, column=1)

            add_button = tk.Button(event_window, text="Add Event", command=lambda: self.add_event(event_id_entry.get(), type_entry.get()))
            add_button.grid(row=2, column=0)

            delete_button = tk.Button(event_window, text="Delete Event", command=lambda: self.delete_event(event_id_entry.get()))
            delete_button.grid(row=2, column=1)

            display_button = tk.Button(event_window, text="Display Event", command=lambda: self.display_event(event_id_entry.get()))
            display_button.grid(row=2, column=2)

        def add_event(self, event_id, type, theme, date, time, duration, venue_address, client_id, guest_ids, supplier_ids,
                      invoice):
            if event_id in self.events:
                messagebox.showerror("Error", "Event with ID already exists.")
            else:
                self.events[event_id] = {
                    "type": type,
                    "theme": theme,
                    "date": date,
                    "time": time,
                    "duration": duration,
                    "venue_address": venue_address,
                    "client_id": client_id,
                    "guest_ids": guest_ids,
                    "supplier_ids": supplier_ids,
                    "invoice": invoice
                }
                self.save_data()
                messagebox.showinfo("Success", "Event added successfully.")

        def delete_event(self, event_id):
            if event_id in self.events:
                del self.events[event_id]
                self.save_data()
                messagebox.showinfo("Success", "Event deleted successfully.")
            else:
                messagebox.showerror("Error", "Event not found.")

        def display_event(self, event_id):
            # Implement display event functionality here

            if event_id in self.events:
                event_details = self.events[event_id]
                messagebox.showinfo("Event Details", f"Event ID: {event_id}\n"
                                                  f"Type: {event_details['type']}\n"
                                                  f"Theme: {event_details['theme']}\n"
                                                  f"Date: {event_details['date']}\n"
                                                  f"Time: {event_details['time']}\n"
                                                  f"Duration: {event_details['duration']} hours\n"
                                                  f"Venue Address: {event_details['venue_address']}\n"
                                                  f"Client ID: {event_details['client_id']}\n"
                                                  f"Guest IDs: {', '.join(event_details['guest_ids'])}\n"
                                                  f"Supplier IDs: {', '.join(event_details['supplier_ids'])}\n"
                                                  f"Invoice: {event_details['invoice']}")
            else:
                messagebox.showerror("Error", "Event not found.")

        def manage_clients(self):
            client_window = tk.Toplevel(self.root)
            client_window.title("Manage Clients")

            tk.Label(client_window, text="Client ID:").grid(row=0, column=0)
            client_id_entry = tk.Entry(client_window)
            client_id_entry.grid(row=0, column=1)

            tk.Label(client_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(client_window)
            name_entry.grid(row=1, column=1)

            add_button = tk.Button(client_window, text="Add Client",
                                   command=lambda: self.add_client(client_id_entry.get(), name_entry.get()))
            add_button.grid(row=2, column=0)

            delete_button = tk.Button(client_window, text="Delete Client",
                                      command=lambda: self.delete_client(client_id_entry.get()))
            delete_button.grid(row=2, column=1)

            display_button = tk.Button(client_window, text="Display Client",
                                       command=lambda: self.display_client(client_id_entry.get()))
            display_button.grid(row=2, column=2)

        def add_client(self, client_id, name):
            if client_id in self.clients:
                messagebox.showerror("Error", "Client with ID already exists.")
            else:
                self.clients[client_id] = name
                self.save_data()
                messagebox.showinfo("Success", "Client added successfully.")

        def delete_client(self, client_id):
            if client_id in self.clients:
                del self.clients[client_id]
                self.save_data()
                messagebox.showinfo("Success", "Client deleted successfully.")
            else:
                messagebox.showerror("Error", "Client not found.")

        def display_client(self, client_id):
            if client_id in self.clients:
                messagebox.showinfo("Client Details", f"Client ID: {client_id}\nName: {self.clients[client_id]}")
            else:
                messagebox.showerror("Error", "Client not found.")

        def manage_guests(self):
            guest_window = tk.Toplevel(self.root)
            guest_window.title("Manage Guests")

            tk.Label(guest_window, text="Guest ID:").grid(row=0, column=0)
            guest_id_entry = tk.Entry(guest_window)
            guest_id_entry.grid(row=0, column=1)

            tk.Label(guest_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(guest_window)
            name_entry.grid(row=1, column=1)

            add_button = tk.Button(guest_window, text="Add Guest",
                                   command=lambda: self.add_guest(guest_id_entry.get(), name_entry.get()))
            add_button.grid(row=2, column=0)

            delete_button = tk.Button(guest_window, text="Delete Guest",
                                      command=lambda: self.delete_guest(guest_id_entry.get()))
            delete_button.grid(row=2, column=1)

            display_button = tk.Button(guest_window, text="Display Guest",
                                       command=lambda: self.display_guest(guest_id_entry.get()))
            display_button.grid(row=2, column=2)

        def add_guest(self, guest_id, name):
            if guest_id in self.guests:
                messagebox.showerror("Error", "Guest with ID already exists.")
            else:
                self.guests[guest_id] = name
                self.save_data()
                messagebox.showinfo("Success", "Guest added successfully.")

        def delete_guest(self, guest_id):
            if guest_id in self.guests:
                del self.guests[guest_id]
                self.save_data()
                messagebox.showinfo("Success", "Guest deleted successfully.")
            else:
                messagebox.showerror("Error", "Guest not found.")

        def display_guest(self, guest_id):
            if guest_id in self.guests:
                messagebox.showinfo("Guest Details", f"Guest ID: {guest_id}\nName: {self.guests[guest_id]}")
            else:
                messagebox.showerror("Error", "Guest not found.")

        def manage_suppliers(self):
            supplier_window = tk.Toplevel(self.root)
            supplier_window.title("Manage Suppliers")

            tk.Label(supplier_window, text="Supplier ID:").grid(row=0, column=0)
            supplier_id_entry = tk.Entry(supplier_window)
            supplier_id_entry.grid(row=0, column=1)

            tk.Label(supplier_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(supplier_window)
            name_entry.grid(row=1, column=1)

            add_button = tk.Button(supplier_window, text="Add Supplier",
                                   command=lambda: self.add_supplier(supplier_id_entry.get(), name_entry.get()))
            add_button.grid(row=2, column=0)

            delete_button = tk.Button(supplier_window, text="Delete Supplier",
                                      command=lambda: self.delete_supplier(supplier_id_entry.get()))
            delete_button.grid(row=2, column=1)

            display_button = tk.Button(supplier_window, text="Display Supplier",
                                       command=lambda: self.display_supplier(supplier_id_entry.get()))
            display_button.grid(row=2, column=2)

        def add_supplier(self, supplier_id, name):
            if supplier_id in self.suppliers:
                messagebox.showerror("Error", "Supplier with ID already exists.")
            else:
                self.suppliers[supplier_id] = name
                self.save_data()
                messagebox.showinfo("Success", "Supplier added successfully.")

        def delete_supplier(self, supplier_id):
            if supplier_id in self.suppliers:
                del self.suppliers[supplier_id]
                self.save_data()
                messagebox.showinfo("Success", "Supplier deleted successfully.")
            else:
                messagebox.showerror("Error", "Supplier not found.")

        def display_supplier(self, supplier_id):
            if supplier_id in self.suppliers:
                messagebox.showinfo("Supplier Details", f"Supplier ID: {supplier_id}\nName: {self.suppliers[supplier_id]}")
            else:
                messagebox.showerror("Error", "Supplier not found.")

        def manage_venues(self):
            venue_window = tk.Toplevel(self.root)
            venue_window.title("Manage Venues")

            # Labels and entry fields for Venue ID and Name
            tk.Label(venue_window, text="Venue ID:").grid(row=0, column=0)
            venue_id_entry = tk.Entry(venue_window)
            venue_id_entry.grid(row=0, column=1)

            tk.Label(venue_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(venue_window)
            name_entry.grid(row=1, column=1)

            # Add Venue button
            add_button = tk.Button(venue_window, text="Add Venue",
                                   command=lambda: self.add_venue(venue_id_entry.get(), name_entry.get()))
            add_button.grid(row=2, column=0)

            # Delete Venue button
            delete_button = tk.Button(venue_window, text="Delete Venue",
                                      command=lambda: self.delete_venue(venue_id_entry.get()))
            delete_button.grid(row=2, column=1)

            # Display Venue button
            display_button = tk.Button(venue_window, text="Display Venue",
                                       command=lambda: self.display_venue(venue_id_entry.get()))
            display_button.grid(row=2, column=2)

        def add_venue(self, venue_id, name):
            if venue_id in self.venues:
                messagebox.showerror("Error", "Venue with ID already exists.")
            else:
                self.venues[venue_id] = name
                self.save_data()  # Save the updated data to the binary file
                messagebox.showinfo("Success", "Venue added successfully.")

        def delete_venue(self, venue_id):
            if venue_id in self.venues:
                del self.venues[venue_id]
                self.save_data()  # Save the updated data to the binary file
                messagebox.showinfo("Success", "Venue deleted successfully.")
            else:
                messagebox.showerror("Error", "Venue not found.")

        def display_venue(self, venue_id):
            if venue_id in self.venues:
                messagebox.showinfo("Venue Details", f"Venue ID: {venue_id}\nName: {self.venues[venue_id]}")
            else:
                messagebox.showerror("Error", "Venue not found.")



    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()



merge_codes()
