import maskpass
from constants import *
import admin, employee

def mainCaller():
    emsLogin = True
    while emsLogin:
        print("====Home Page====")

        print("""
        1. Login As Admin
        2. Login As Employee
        3. Quit
        """)

        choice = input("Enter your choice : ")

        if choice == "1":

            print("====Welcome to Admin Panel====")
            admin_id = input("Enter Admin ID : ")
            # admin_pwd = input("Enter Admin Password : ")
            admin_pwd = maskpass.advpass()
            # print(admin_pwd)
            
            if admin_id == ADMIN_ID and admin_pwd == ADMIN_PASSWORD:
                print("Login Success...")
                adminLogin = True
                while adminLogin:

                    print("""
            1. Add New Employee
            2. Delete An Employee
            3. Update An Employee
            4. Search An Employee
            5. Print All Employees
            Q. Quit/Log Out
            """)
                    
                    adminChoice = input("Enter your choice : ")

                    operations = {
                        "1" : admin.addNewEmployee,
                        "2" : admin.deleteEmployees,
                        "3" : admin.updateEmployee,
                        "4" : admin.searchEmployee,
                        "5" : admin.printAllEmployees,
                        "Q" : exit,  # exit is a pre-defined function
                        "q" : exit
                    }

                    operations.get(adminChoice, admin.invalidChoice)()

                else:
                    print("Login Failed...Invalid ID or Password")

        elif choice == "2":
            employee.loginEmployee()
        
        elif choice == "3":
            break

        else:
            print("Invalid Choice...")

mainCaller()