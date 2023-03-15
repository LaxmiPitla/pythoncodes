#Final Project Building calculator programmm


import re #importing regEX library/module

print("our magical calulator")
print("Enter 'quit' to exit program")
previous=0                          #it holds the previous value
run = True                             #initialiizing run value to 1/true


def do_math():                                          #defining function
    global run                                          #using global run in function
    global previous                                     #using global previous in function
    if previous == 0:                                   #condition
        equation = input("Enter the equation:")         #taking euation from user
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Good bye hoomans")                       #last statement to display
        run = False                                     #chnaging for while loop to be false
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        #regex for eliminating charaters,special chars becoz eval might crash the system
        if previous == 0:
            previous = eval(equation)                   #calculate first equation
        else:
            previous = eval(str(previous) + equation)       #cal second equation to previously calculated one

while run:
    do_math()
