def add(num1, num2):
   pass
 
def subtract(num1, num2):
   pass
 
def multiply(num1, num2):
   pass
 
def divide(num1, num2):
   pass
 
 
 
def run():
   num1 = input("Provide number 1: ")
   num2 = input("Provide number 2: ")
   operation = input("Provide operation to perform (+ - x %): ")
 
   if operation == "+":
       add(num1, num2)
 
   elif operation == "-":
       subtract(num1, num2)
  

   elif operation == "x":
       multiply(num1, num2)
 
   elif operation == "%":
       divide(num1, num2)
  
run()
