from CalculatorArt import logo


def add(n1, n2):
  return n1 + n2

def substruct(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substruct,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for sign in operations:
    print(sign)
  should_cont = True

  while should_cont: 
    operation_sign = input("Which operation do you want to use?: ")
    num2 = float(input("What's the next number?: "))
    operation_function = operations[operation_sign]
    result = operation_function(num1, num2)
    print(f"{num1} {operation_sign} {num2} = {result}")

    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':  
      num1 = result
    else: 
      should_cont = False
      calculator()

calculator()