# Author Andre Hoarau
def main ():
    display_menu
    while True:
        choice = input("Enter choice: ")
        if (choice == "x"):
            break
    
def display_menu():
    print("Conference Management")
    print("---------------------")
    print("===")
    print("1 - View Spearker & Sessions")
    print("2 - View Attendees by Company")
    print("3 - Add New Attendee")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("x - Exit Application")
