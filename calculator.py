num1= float(input("enter the first number:"))
operator=input("enter the operator(+,-,*,/):")
num2 = float(input("enter the second number: "))

if operator == '+':
   print("Result=",num1+num2)
elif operator == '-':
   print ("result=",num1-num2)
elif operator == '*':
   print('result=',num1*num2)
elif operator == '/':
   if num2!=0:
      print("Result=",num1/num2)
   else:
      print("cannot divide by zero")
else:
      print("invalid oiprator!")   
