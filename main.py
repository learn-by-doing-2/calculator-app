def add(num1, num2):
   """
   Finds the sum of two numbers.
   """
   result = int(num1) + int(num2)
   print(f"The sum of {num1} and {num2} is {result}")
 
def subtract(num1, num2):
   """
   Find the difference between two numbers.
   """
   result = int(num1) - int(num2)
   print(f"The difference between {num1} and {num2} is {result}")
 
def multiply(num1, num2):
   """
   Finds the product of two numbers.
   """
   result = int(num1) * int(num2)
   print(f"The product of {num1} and {num2} is {result}")
 
def divide(num1, num2):
   """
   Finds the division of two numbers.
   """
   result = int(num1) / int(num2)
   print(f"The result of dividing {num1} by {num2} is {result}")
 
 
 
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
