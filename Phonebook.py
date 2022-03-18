import sqlite3 as sql

from jinja2 import pass_eval_context

connection = sql.connect("phonebook.db")
c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS phonebook (firstname TEXT, lastname TEXT, phonenumber TEXT, streetaddress TEXT)")

choice = None
while choice != "5":
    print("1: Add person to phone book")
    print("2: Update records")
    print("3: Remove recods")
    print("4: Display phone book")
    print("5: Quit")
    choice = input("> ")
    print()
    
    if choice == "1":
        
        try:
            firstname = input("first name: ")
            lastname = input("last name: ")
            phonenumber = input("phone number: ")
            streetaddress = input("street address: ")
            values = (firstname, lastname, phonenumber, streetaddress)
            
            c.execute("INSERT INTO phonebook VALUES (?,?,?,?)", values)
            connection.commit()
            
        except ValueError:
            print("Invalid Info")
            
    if choice == "2":
        try:
            change_choice = None
            while change_choice != True:
                print("1: change fist name")
                print("2: change last name")
                print("3: change phone number")
                print("4: change address")
                print()
                change = input("> ")
                
                phonenumber = input("phone number: ")
                # change first name
                if change == "1":
                    firsttnamechange = input("What would you like to change the first name to? ")
                    values = (firsttnamechange, phonenumber)
                    c.execute("UPDATE phonebook SET firstname = ? WHERE phonenumber = ?", values)
                    connection.commit()
                    change_choice = True
                    
                # change last name     This still needs to be fixed
                if change == "2":
                    lastnamechange = input("What would you like to change the last name to? ")
                    values = (lastnamechange, phonenumber)
                    c.execute("UPDATE phonebook SET lasttname = ? WHERE phonenumber = ?", values)
                    connection.commit()
                    change_choice = True
                    
                # change phonenumber
                if change == "3":
                    phonenumberchange = input("What would you like to change the phone number to? ")
                    values = (phonenumberchange, phonenumber)
                    c.execute("UPDATE phonebook SET phonenumber = ? WHERE phonenumber = ?", values)
                    connection.commit()
                    change_choice = True
                    
                # change street address
                if change == "4":
                    addresschange = input("What would you like to change the street address to? ")
                    values = (addresschange, phonenumber)
                    c.execute("UPDATE phonebook SET streetaddress = ? WHERE phonenumber = ?", values)
                    connection.commit()
                    change_choice = True
                    
        except ValueError:
            print("Invalid Info")

    if choice == "3":
        phonenumber = input("what is the phone number you wish to remove: ")
        values = (phonenumber, )
        c.execute("DELETE FROM phonebook WHERE phonenumber = ?", values)
        
    if choice == "4":
        c.execute("SELECT * FROM phonebook Order by lastname desc")
        print("{:>15} {:>15} {:>15} {:>15}".format("firstname", "lastname", "phonenumber", "streetaddress"))
        for record in c.fetchall():
            print("{:>15} {:>15} {:>15} {:>15}".format(record[0], record[1], record[2], record[3]))