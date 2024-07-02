persons = {
    1: {
        "Name": "John",
        "Age" : "37",
        "Gender" : "Male",
        "Occupation" : "Lawyer",
    }, 2 : {
        "Name": "Helen",
        "Age" : "42",
        "Gender" : "Female",
        "Occupation" : "Doctor",
    }, 3 : {
        "Name": "Ross",
        "Age" : "25",
        "Gender" : "Male",
        "Occupation" : "Cool Dude",
    }
}
        
def add_contact(person_id="Numeric ID"):
     valid_input = False
     while True:
        print(f"Adding another person as: person {len(persons)+1}")
        while (valid_input == False):
            name = input("Please enter a name: ").capitalize()
            try:
                age = int(input("Please enter their age: "))
                valid_input = True
            except ValueError:
                print("You need to enter a numerical value")
        gender = input("Please enter a gender: ").capitalize()
        occupation = input("Please enter an occupation: ").capitalize()
        if (valid_input == True):
            persons[(len(persons)+ 1)] = {"Name" : name, "Age" : age, "Gender" : gender, "Occupation" : occupation}
            return
       

def del_contact(person_id=None):
    while True:
        person_to_delete = get_contact()
        delete_check = input(f"Are you sure you want to delete:\n\n Person ID = {person_id}, Name: {person_to_delete}?\n\n           Y/N: ").upper()
        if delete_check == "Y":
            del persons[person_id]


def display_contacts():
    for person_id, info in persons.items():
        print("\nPerson:", person_id)
        for field in info:
            print(f"{field}: {info[field]}") 

def display_contact(person_id=None):
    if person_id is None:
        contact = persons[get_contact()]
    else:
        contact = persons[person_id]
    print(f"\n--- Contact {person_id} ---\n")
    print(f"Name: {contact["Name"]}\nAge: {contact["Age"]}\nGender: {contact["Gender"]}\nOccupation: {contact["Occupation"]}" )
    print("\n-----------------")
        
def get_yes_no(choice):
    yes = {'yes','y', 'ye'}
    no = {'no','n'}
    while True:
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            choice = input("Please enter a valid response.\n").lower()

def perform_another_action(add=None):
    perform_another = input(f"Would you like to perform this action again?\n Y/N").lower()
    if get_yes_no(perform_another):
        person_id = get_contact()
        while True:
            try:
                if add is not None:
                    if person_id not in persons:
                        break
                    else:
                        print("That Person ID number is already taken.")
                else:
                    break
            except ValueError:
                print("Error in function perform_another_action.")

        return person_id
    
    return None

def get_contact():
    while True:
        try:
            person_id = int(input("Please select a contact using their Person ID number"))
            if person_id in persons:
                break
            else:
                print("That was not a valid Person ID number.")
        except (ValueError, KeyError):
            print("The Person ID number you entered was incorrect.")
    return person_id

# Will need some way to verify the input is appropriate?
# Will attempt to add this change to the new branch
def get_contact_details(choice):
    match choice:
        case "all":
            while True:
                    name = input("Please enter a name: ").capitalize()
                    try:
                        age = int(input("Please enter their age: "))
                        valid_input = True
                    except ValueError:
                        print("You need to enter a numerical value")
                    gender = input("Please enter a gender: ").capitalize()
                    occupation = input("Please enter an occupation: ").capitalize()
                    return name, age, gender, occupation
        case "name":
            name = input("Please enter a name: ").capitalize()
        case "age":
            while (valid_input == False):
                try:
                    age = int(input("Please enter their age: "))
                    valid_input = True
                except ValueError:
                    print("You need to enter a numerical value")
        case "gender":
            gender = input("Please enter a gender: ").capitalize()
        case "occupation":
            occupation = input("Please enter an occupation: ").capitalize()



def edit_contact():
    print("\nWhich contact would you like to edit?\n")
    contact = get_contact()
    display_contact(contact)
    while True:
        try:
            print("--- Menu Choices ---")
            print("1 : Change All\n2 : Change Name\n3 : Change Age\n4 : Change Gender\n5 : Change Occupation\n")
            print("-----------------")
            menu_selection = int(input("\nPlease select an option: "))
            if menu_selection in range(1,5):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid menu selection.")
    if menu_selection == 1:
        print("--- Editing all ---")
        get_contact_details("all")

edit_contact()
        
    

def main():
    print("--- Contacts Menu ---")

if __name__ == "__main__":
    main()

