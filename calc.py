def main():
  # 계산식 선택
  print("Select calculation. add or divide")
  calc = str(input("calc: "))
  # 숫자 선택
  print("Type two numbers for x and y")
  x = int(input("x > "))
  y = int(input("y > "))
  # 더하기
  if calc == add: 
    print("%d + %d = %d" % (x, y, add(x, y)))
  # 나누기
  elif calc == divide:
    if y != 0:
      print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    else:
      divide(x,y)
  # 계산식 선택 X
  else:
    print ("Please select between add and divide")
    main()  
# add 함수
def add(): 
  return x+y
# divide 함수
def divide():
  if y==0:
        print("Error: cannot divide by zero.")
    else:
        return x/y

if __name__ == "__main__":
    main()
  
