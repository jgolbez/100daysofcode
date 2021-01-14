def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calc_result(firstnum, secnum, oper_funct):
  result = operations[oper_funct](firstnum, secnum)
  return result

def calculator():
  number1 = float(input("What is the first number?\n"))
  continue_calc = True
  answer = None
  while continue_calc:
    for math_symbol in operations:
      print(math_symbol)
    op_symbol = input("What operation will you use? Choose from above list.\n")
    number2 = float((input("What is the next number?\n")))
    if answer == None:
      answer = calc_result(number1, number2, op_symbol)
      print(f"{number1} {op_symbol} {number2} = {answer}")
    else:
      prev_answer = answer
      answer = calc_result(answer, number2, op_symbol)
      print(f"{prev_answer} {op_symbol} {number2} = {answer}")
    continue_calc = bool(input(f"Continue calculating with {answer}? Y or N\n").upper() == "Y")
    
calculator()