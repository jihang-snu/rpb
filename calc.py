def main():
  # 계산식 선택
  print("Select calculation. add, subtract, multiply, divide")
  calc = input("calc: ")
  # 숫자 선택
  print("Type two numbers for x and y")
  x = int(input("x > "))
  y = int(input("y > "))
  # 더하기
  if calc == "add": 
    print("%d + %d = %d" % (x, y, add(x, y)))
  # 빼기
  elif calc == "subtract":
    print("%d - %d = %d" % (x, y, subtract(x, y)))
  # 곱하기
  elif calc == "multiply":
    print("%d * %d = %d" % (x, y, multiply(x, y)))
  # 나누기
  elif calc == "divide":
    if y != 0:
      print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    else:
      divide(x,y)
  # 계산식 선택 X
  else:
    print ("Please select between add and divide")
    main()  
# add 함수
def add(x,y): 
  return x+y
# subtract 함수
def subtract(x,y):
  return x-y
# multiply 함수
def multiply(x,y):
  return x*y
# divide 함수
def divide(x,y):
  if y==0:
    print("Error: cannot divide by zero.")
  else:
    return x/y

if __name__ == "__main__":
    main()
