def add(var1,var2):  #Addition function 
    return var1+var2

def difference(var1,var2):  #subtraction function
    return var1-var2

def div(var1,var2):   #division function
    return var1/var2

def product(var1,var2):  #Multiplication function
    return var1*var2


print("------------------------------CALCULATOR 1.0--------------------------------- ")#instruction for the user
print("""  Enter----->                                                           
      + ---- Additon
      - ---- Subtraction
      * ---- product
      / ---- Division
      exit --- To exit 
      """)

while True:# While loop is initiated to peform operations multiple times 
   
    choice = input("Enter operation you want to perform : ")#choice variables will take users choice 
    
    if choice=="+":    #Addition case
         value1 = input("Enter first number: ")   #user input will be taken here in string format for addition case
         value2 = input("Enter second number: ")
         value1 = float(value1)
         value2 = float(value2) 
         
         print("sum = "+str(add(value1,value2))) #Output to the user if the condition is satisfied
        
    elif choice=="-": #subraction case
         value1 = input("Enter first number: ")#user input will be taken here in string format for addition case
         value2 = input("Enter second number: ")
        #string is converted to float values for mathematical calculation
         value1 = float(value1)
         value2 = float(value2)
         print("difference = "+str(difference(value1,value2))) #Output to the user if the condition is satisfied
    
    elif choice=="*":#Multipication case
         value1 = input("Enter first number: ")#user input will be taken here in string format for addition case
         value2 = input("Enter second number: ")
         #string is converted to float values for mathematical calculation
         value1 = float(value1)
         value2 = float(value2)
         print("multiplication = "+str(product(value1,value2)))#Output to the user if the condition is satisfied
       
    elif choice=="/":#division case
         value1 = input("Enter first number: ")#user input will be taken here in string format for addition case
         value2 = input("Enter second number: ")
         #string is converted to float values for mathematical calculation
         value1 = float(value1)
         value2 = float(value2)
         if value2==0.0:
           print(" Enter the valid second value")
         else:      
           print("division = "+str(div(value1,value2)))#Output to the user if the condition is satisfied
         
    elif choice == "exit":   #exit condition to terminate the program
        break
    else:
        print("Enter a valid value")    #Else condition will be used if user enters incorrect choice 


