from constants import *

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
    for emp in employees:
        if emp['ID'] == empID:
            print("Employee Logged in Successfully...")
            return emp['ID']
    else:
        print("Employee Not Found...")
        return False


def printAllEmployees():
    for emp in employees:
        for key in emp:
            print(key, ":", emp[key])
        print("=====================")

def invalidChoice():
    print("You have pressed some wrong button...")