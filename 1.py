#Add a student record
#View all records
#Search a student by name/roll
#Update a student record
#Delete a student record
import json

def add_menu():
    try:
        with open("record.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    students ={
        "name": name,
        "roll": roll,
        "age": age,
        "marks": marks
    }
    data.append(students)

    with open("record.json", "w") as f:
        json.dump(data, f, indent = 4)

    print("Student added successfully!!")
    return

def view_students():
    try:
        with open("record.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No record file found!")
        return
    except json.decoder.JSONDecodeError:
        print("Record file is empty or corrupted.")
        return
    if not data:
        print("No student records found.")
        return
    print("Students records: ")
    for student in data:
        print(f"Name: {student['name']}\n Roll: {student['roll']}\n Age: {student['age']}years\n Marks: {student['marks']}")
def search_students():
    try:
        with open("record.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No record file found!")
        return
    except json.decoder.JSONDecodeError:
        print("Record file is empty or corrupted.")
        return
    if not data:
        print("No student records found.")
        return
    keyword = input("Enter name or roll no. to search: ").strip().lower()
    found = False
    for student in data:
        if student['name'].lower() == keyword or student['roll'] == keyword:
            print(f"Name: {student['name']}\n Roll: {student['roll']}\n Age: {student['age']}years\n Marks: {student['marks']}")
            found= True
        if not found:
            print("No matching student found!!")
            
def update_student():
    try:
        with open("record.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No record file found!")
        return
    except json.decoder.JSONDecodeError:
        print("Record file is empty or corrupted.")
        return
    if not data:
        print("No students record found!")
        return
    
    roll_to_update = input("Enter the roll no of student to update: ").strip()
    for student in data:
        if student['roll']==roll_to_update:
            print("Student Found. Leave a field to keep it unchanged.")
            new_name = input(f"Enter the new name{student['name']}: ")
            new_age = input(f"Enter the new age{student['age']}: ")
            new_marks= input(f"Enter the new marks{student['marks']}: ")
            if new_name:
                student['name']=new_name
            if new_age:
                student['age']= int(new_age)
            if new_marks:
                student['marks']= float(new_marks)
            
            with open("record.json", "w")as f:
                json.dump(data, f, indent=4)
            print("Student records updated successfully!")
            return
        print("Student with this roll number not found.")

def delete_student():
    try:
        with open("record.json", "r")as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No record file found.")
        return
    except json.decoder.JSONDecodeError:
        print("Record file is empty or corrupted")
        return
    if not data:
        print("No student record found!")
        return
    delete_stu = input("Enter the roll number of student to delete: ").strip()
    for roll in data:
      if roll == delete_stu:
        confirm = input(f"Are you sure you want to delete {roll['name']}? Yes or No").lower()
        if confirm == "yes":
            del data[roll]
            with open("record.json", "w")as f:
                json.dump(data, f, indent=4)
            print("Student deleted successfully!")
        else:
            print("Deletion failed!")
      else:
          print("No student found with that roll no.!")
          return
      
def menu():
    choices = ["Add a student record", "View all records", "Search a student by name/roll", "Update a student record", "Delete a student record", "Exit"]
    for i, item in enumerate(choices):
        print(f"{i+1}. {item}")
    choice = int(input("Enter the task number: "))
    while True:
      if choice == 1:
        add_menu()
      elif choice == 2:
        view_students()
      elif choice ==3:
        search_students()
      elif choice == 4:
        update_student()
      elif choice == 5:
        delete_student()
      elif choice == 6:
        print("Thank you for your presence")
        break
        
def menu():
    choices = ["Add a student record", "View all records", "Search a student by name/roll", "Update a student record", "Delete a student record", "Exit"]
    for i, item in enumerate(choices):
        print(f"{i+1}. {item}")
    choice = int(input("Enter the task number: "))
    while True:
        if choice == 1:
            add_menu()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_students()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Thank you for your presence")
            break

        # ⬇️ Added part: ask whether to continue or stop
        cont = input("\nDo you want to perform another task? (yes/no): ").strip().lower()
        if cont == "yes":
            for i, item in enumerate(choices):
                print(f"{i+1}. {item}")
            choice = int(input("Enter the task number: "))
        else:
            print("Exiting program. Goodbye!")
            break

menu()