# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit



def add(a,b):
    answer= a + b
    print (str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer= a - b
    print (str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
    answer= a * b
    print (str(a) + " * " + str(b) + " = " + str(answer))

def div(a,b):
    answer= a / b
    print (str(a) + " / " + str(b) + " = " + str(answer))
    
while True:
   a= int(input ("Please enter your first number :"))
   options= input (" Please select + , / , * or  -  : ")
   b= int(input ("Please enter your second number :"))

   if options=="+":
    add(a,b)
   elif options=="-":
    add(a,b)
   elif options=="*":
    mul(a,b)
   elif options=="/":
    div(a,b)
   else:
    print("Please enter correct option  ( + , * , - , / )")
    
