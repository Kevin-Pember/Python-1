#Part 1
contacts = {}
running = True
while running:
    print("Phonebook Menu\n1. Add new contact\n2. Search for a contact\n3. Display all Contacts\n4. Exit")
    print()
    option = int(input("Enter the number for the option you want to perform: "))
    if(option == 1):
        name = input("Enter the name: ")
        contacts[name] = input("Enter the phone number: ")
        print("Contact added successfully!")
    elif(option == 2):
        usrIn = input("Enter the name: ")
        if usrIn in contacts:
            print(usrIn+": "+contacts[usrIn])
        else:
            print("Contact not found in the phonebook.")
    elif(option == 3):
        count = 0
        for contact in contacts:
            count += 1
            print(str(count)+". "+contact+": "+contacts.get(contact))
    else:
        running = False
    print()