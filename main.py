# Author Andre Hoarau
import mysqldbaccess
import myneo4jaccess
def main ():
    display_menu()
    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            name = input("Enter speaker name : ")
            print(f"session details for : {name}")
            print("--------------------------------")
            speakers = mysqldbaccess.find_speaker(name)
            if speakers:

                for speaker in speakers:
                    print(speaker["speakerName"],"|",speaker["sessionTitle"],"|",speaker["roomName"])
            else:
                print("No speakers found of that name")
            print("--------------------------------")
            display_menu()
        elif (choice == "2"):

            while True:
            
                compid = input("Enter company ID: ")

                if compid.isdigit() and int(compid) > 0:
                
                    compid = int(compid)

                    company = mysqldbaccess.company_exists(compid)

                    if not company:
                        print("Company does not exist.")
                        continue

                    company_data = mysqldbaccess.find_comp(compid)

                    if not company_data:
                        print("Company exists but has no attendees registered for sessions.")
                        continue

                    print("")
                    print("Company:", company_data[0]["companyName"])
                    print("--------------------------------")

                    for attendee in company_data:
                    
                        print(
                            attendee["attendeeName"], "|",
                            attendee["attendeeDOB"], "|",
                            attendee["sessionTitle"], "|",
                            attendee["speakerName"], "|",
                            attendee["sessionDate"], "|",
                            attendee["roomName"]
                        )

                    print("--------------------------------")
                    display_menu()

                    break

                else:
                    print("Invalid company ID. Please enter a positive integer.")
        
        elif (choice =="3"):
                id = input("Attendee ID: ")
                name = input("Name: ")
                dob = input("DOB: ")
                gender = input("Gender: ")
                id_att_comp = input("Company ID: ")
                mysqldbaccess.add_attendee(id,name,dob,gender,id_att_comp)
                print("--------------------------------")
                display_menu()
        
        elif (choice =="4"):
                id_input = int(input("Attendee ID: "))
                target_name = mysqldbaccess.get_name_by_id(id_input)
                if not target_name:
                    print(f"No attendee found with ID {id_input}")
                else:
                    print(f"\nAttendee: {target_name} (ID: {id_input})")
                    print("Connected to:")
                    print("--------------------------------")
                
                # 2. Use Neo4j to get the list of connected IDs
                connected_ids = myneo4jaccess.get_connections_list(id_input)
                
                if not connected_ids:
                    print("No connections found for this attendee.")
                else:
                    # 3. For every ID Neo4j found, ask MySQL for the Name
                    for c_id in connected_ids:
                        c_name = mysqldbaccess.get_name_by_id(c_id)
                        print(f"{c_id} | {c_name}")
            
                print("--------------------------------")
                display_menu()
        
        elif(choice=="5"):
            id1 = input("Attendee ID 1: ")
            id2 = input("Attendee ID 2: ")
            if not (id1.isdigit() and id2.isdigit()):
                print("Error: Attendee IDs must be numeric.")
                continue
            if id1 == id2:
                print("Error: An attendee cannot be CONNECTED_TO him/herself.")
                continue
            name1 = mysqldbaccess.get_name_by_id(id1)
            name2 = mysqldbaccess.get_name_by_id(id2)

            if not name1 or not name2:
                print("Error: One or both attendees do not exist in the MySQL database.")
            else:
                # 4. Attempt to create connection (Neo4j will check for existing links)
                success = myneo4jaccess.create_connections(id1, id2)
                
                if success:
                    print(f"Successfully connected {name1} and {name2}.")
                else:
                    print(f"Error: {name1} and {name2} are already connected.")

            print("--------------------------------")
            display_menu()

        elif (choice == "x"):
            break
    
def display_menu():
    print("Conference Management")
    print("---------------------")
    print("===")
    print("1 - View Speaker & Sessions")
    print("2 - View Attendees by Company")
    print("3 - Add New Attendee")
    print("4 - View Connected Attendees")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("x - Exit Application")

if __name__ =="__main__":
    main()