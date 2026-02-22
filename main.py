import string
from pyscript import *

def password_checkerv1():
    if len(document.getElementById("username_inp").value) < 7:
        return "Username not long enough"
    else:
        if not document.getElementById("username_inp").value.isalpha():
            if not document.getElementById("username_inp").value.isdigit():
                print("Valid")
            else:
                return "Please include letters on your username"
        else:
            return "Please include digits on your username"


    pass_grab = document.getElementById("password_inp").value

    for char in pass_grab:
        if char in list(string.punctuation):
            return "No Special Characters on your password"
    
    if len(pass_grab) < 10:
        return "Password not long enough"



    if not pass_grab.isalpha():
        if not pass_grab.isdigit():
            return True
        else:
            return "Please include letters on your password"
    else:
        return "Please include digits on your password"



def check_pass(e):
    document.getElementById("output").innerHTML = ""
    result = password_checkerv1()

    if result == True:
        document.getElementById("output").style.color = "green"
        document.getElementById("output").innerHTML = f"Your account is valid. Welcome, {document.getElementById("username_inp").value}"
    else:
        document.getElementById("output").style.color = "red"
        document.getElementById("output").innerHTML = result

    