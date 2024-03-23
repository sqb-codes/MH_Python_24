import maskpass
from constants import *

def loginEmployee():
    print("====Welcome to Employee Dashboard====")
    empID = input("Enter Emp ID : ")
    # empPwd = input("Enter Emp Password : ")
    empPwd = maskpass.askpass(mask="")
    for emp in employees:
        if emp['ID'] == empID and emp['Pwd'] == empPwd:
            print("Employee Logged in Successfully...")
            for key in emp:
                print(key, ":", emp[key])
            break
    else:
        print("Employee Not Found...")
