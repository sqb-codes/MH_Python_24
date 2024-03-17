employees = []

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
        admin_pwd = input("Enter Admin Password : ")
        
        if admin_id == "123A" and admin_pwd == "DU@mhAdmin":
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
                if adminChoice == "1":
                    print("Adding New Employee...")
                    empId = input("Enter Emp ID : ")
                    empName = input("Enter Emp Name : ")
                    empSalary = input("Enter Emp Salary : ")
                    empDept = input("Enter Emp Department : ")
                    empPwd = empId + "@" + empName.split()[0]

                    emp = {"ID" : empId, "Name" : empName, "Pwd" : empPwd, "Salary" : empSalary, "Dept" : empDept}
                    employees.append(emp)

                    print("New Employee Added Successfully...")

                elif adminChoice == "2":
                    pass
                elif adminChoice == "3":
                    pass
                elif adminChoice == "4":
                    pass
                elif adminChoice == "5":
                    for emp in employees:
                        for key in emp:
                            print(key, ":", emp[key])
                        print("=====================")
                
                elif adminChoice == "Q" or adminChoice == "q":
                    adminLogin = False
                    break
                else:
                    print("Invalid Choice")

            else:
                print("Login Failed...Invalid ID or Password")


    elif choice == "2":
        print("====Welcome to Employee Dashboard====")
        empID = input("Enter Emp ID : ")
        empPwd = input("Enter Emp Password : ")
        for employee in employees:
            if employee['ID'] == empID and employee['Pwd'] == empPwd:
                print("Employee Logged in Successfully...")
                for key in employee:
                    print(key, ":", employee[key])
                break
        else:
            print("Employee Not Found...")
    
    elif choice == "3":
        break

    else:
        print("Invalid Choice...")