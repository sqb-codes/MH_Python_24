import maskpass

employees = []

def addNewEmployee():
    print("Adding New Employee...")
    empId = input("Enter Emp ID : ")
    empName = input("Enter Emp Name : ")
    empSalary = input("Enter Emp Salary : ")
    empDept = input("Enter Emp Department : ")
    empPwd = empId + "@" + empName.split()[0].lower()

    emp = {"ID" : empId, "Name" : empName, "Pwd" : empPwd, "Salary" : empSalary, "Dept" : empDept}
    employees.append(emp)

    print("New Employee Added Successfully...")


def deleteEmployees():
    emp = input("Enter Employee ID : ")
    # reuse logic of search
    searchResult = searchEmployee()
    if searchResult:
        pass
    else:
        pass


def updateEmployee():
    emp = input("Enter Employee ID : ")
    # reuse logic of search
    searchResult = searchEmployee()
    if searchResult:
        # Now ask what you want to update : Name, Salary, Department
        pass
    else:
        pass


def searchEmployee():
    empID = input("Enter Employee ID : ")
    # logic to search employee
    for employee in employees:
        if employee['ID'] == empID:
            print("Employee Logged in Successfully...")
            return employee['ID']
    else:
        print("Employee Not Found...")
        return False


def printAllEmployees():
    for emp in employees:
        for key in emp:
            print(key, ":", emp[key])
        print("=====================")


def loginEmployee():
    print("====Welcome to Employee Dashboard====")
    empID = input("Enter Emp ID : ")
    # empPwd = input("Enter Emp Password : ")
    empPwd = maskpass.askpass(mask="")
    for employee in employees:
        if employee['ID'] == empID and employee['Pwd'] == empPwd:
            print("Employee Logged in Successfully...")
            for key in employee:
                print(key, ":", employee[key])
            break
    else:
        print("Employee Not Found...")


def invalidChoice():
    print("You have pressed some wrong button...")


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
        
        if admin_id == "123A" and admin_pwd == "du@mhadmin":
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
                    "1" : addNewEmployee,
                    "2" : deleteEmployees,
                    "3" : updateEmployee,
                    "4" : searchEmployee,
                    "5" : printAllEmployees,
                    "Q" : exit,  # exit is a pre-defined function
                    "q" : exit
                }

                operations.get(adminChoice, invalidChoice)()

            else:
                print("Login Failed...Invalid ID or Password")

    elif choice == "2":
        loginEmployee()
    
    elif choice == "3":
        break

    else:
        print("Invalid Choice...")