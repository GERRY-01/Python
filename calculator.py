#  a function called calculator that takes two numbers and an operation (+, -, *, /) as arguments 
# and returns the result of the operation.

def calculator(num1 : int, num2 : int, operator :str):
    if operator == "+" :
      result  = num1 + num2
      return result
    
    elif operator == "-" :
        result = num1 - num2
        return result
               
    elif operator == "*" :
        result = num1 * num2
        return result
        
    elif operator == "/" :
        result = num1 / num2
        return result
          
    else :
        return "Invalid operator"

print(calculator(4,8,"*"))