import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Complaint:
    """
    Represents a customer complaint.

    Attributes:
        customer_name (str): The name of the customer.
        subject (str): The subject of the complaint.
        complaint_description (str): The description of the complaint.
        category (str): The category of the complaint.
        timestamp (datetime): The timestamp when the complaint was created.
    """
    def __init__(self, customer_name, subject, complaint_description, category):
        self.customer_name = customer_name
        self.subject = subject
        self.complaint_description = complaint_description
        self.category = category
        self.timestamp = datetime.now()


class ComplaintGUI:
    """
    GUI for the Complaint Management System.

    Attributes:
        complaints (list): List to store the Complaint objects.
        window (Tk): The main application window.
        customer_name_label (Label): Label for customer name input.
        customer_name_entry (Entry): Entry field for customer name input.
        subject_label (Label): Label for subject input.
        subject_entry (Entry): Entry field for subject input.
        complaint_description_label (Label): Label for complaint description input.
        complaint_description_entry (Entry): Entry field for complaint description input.
        category_label (Label): Label for category selection.
        category_variable (StringVar): Variable to store the selected category.
        add_button (Button): Button to add a new complaint.
        display_button (Button): Button to display all complaints.
    """
    def __init__(self):
        self.complaints = []

        # Create the main application window
        self.window = tk.Tk()
        self.window.title('Complaint Management System')

        # Create labels and entry fields for customer name, subject, and complaint description
        self.customer_name_label = tk.Label(self.window, text='Customer Name')
        self.customer_name_label.pack()
        self.customer_name_entry = tk.Entry(self.window)
        self.customer_name_entry.pack()

        self.subject_label = tk.Label(self.window, text='Subject')
        self.subject_label.pack()
        self.subject_entry = tk.Entry(self.window)
        self.subject_entry.pack()

        self.complaint_description_label = tk.Label(self.window, text='Complaint Description')
        self.complaint_description_label.pack()
        self.complaint_description_entry = tk.Entry(self.window)
        self.complaint_description_entry.pack()

        # Create label and option menu for category selection
        self.category_label = tk.Label(self.window, text='Category')
        self.category_label.pack()
        self.category_variable = tk.StringVar(self.window)
        self.category_variable.set('Technical')  # Default category is Technical
        self.category_option_menu = tk.OptionMenu(self.window, self.category_variable, 'Technical', 'Billing', 'Delivery')
        self.category_option_menu.pack()

        # Create buttons for adding a complaint and displaying complaints
        self.add_button = tk.Button(self.window, text='Add Complaint', command=self.add_complaint)
        self.add_button.pack()
        self.display_button = tk.Button(self.window, text='Display Complaints', command=self.display_complaints)
        self.display_button.pack()

        # Bind the Enter key press event to the add_complaint method
        self.window.bind('<Return>', self.add_complaint)

        # Run the GUI application.
        self.window.mainloop()

    def add_complaint(self, event=None):
        """
        Add a new complaint to the system.
        """
        customer_name = self.customer_name_entry.get()
        subject = self.subject_entry.get()
        complaint_description = self.complaint_description_entry.get().strip()
        
        # Get the selected category
        category = self.category_variable.get()

        # Validate input fields
        if not customer_name or not subject or not complaint_description:
            messagebox.showwarning('Missing Information', 'Please fill in all fields.')
            return

        # Create a new Complaint object
        complaint = Complaint(customer_name, subject, complaint_description, category)
        self.complaints.append(complaint)
        messagebox.showinfo('Complaint Added', 'Complaint added successfully!')

        # Clear input fields
        self.customer_name_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.complaint_description_entry.delete(0, tk.END)

        # Write complaint data to file
        with open('complaints.txt', 'a') as file:
            file.write(f'Customer Name: {complaint.customer_name}\n')
            file.write(f'Subject: {complaint.subject}\n')
            file.write(f'Complaint Description: {complaint.complaint_description}\n')
            file.write(f'Category: {complaint.category}\n')
            file.write(f'Timestamp: {complaint.timestamp}\n\n')

    def display_complaints(self):
        """
        Display all the complaints in the system.
        """
        if not self.complaints:
            messagebox.showinfo('No Complaints', 'No complaints found.')
        else:
            # Sort complaints based on timestamp in descending order
            sorted_complaints = sorted(self.complaints, key=lambda x: x.timestamp, reverse=True)

            complaint_details = ''
            for complaint in sorted_complaints:
                complaint_details += f'Customer Name: {complaint.customer_name}\n'
                complaint_details += f'Subject: {complaint.subject}\n'
                complaint_details += f'Complaint Description: {complaint.complaint_description}\n'
                complaint_details += f'Category: {complaint.category}\n'
                complaint_details += f'Timestamp: {complaint.timestamp}\n\n'

            messagebox.showinfo('Complaints', complaint_details)

complaint_system = ComplaintGUI()
