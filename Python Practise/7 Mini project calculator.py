first = input ("Enter first number : ")
operator = input ("Enter operator(+,-,*,/,%) : ")
second = input ("Enter Second Number : ")

first = int (first)
second = int(second)

if operator == "+" :
    print (first + second)
elif operator == "-" :
    print (first - second)
elif operator == "*" :
    print (first * second)
elif operator == "/" :
    print (first / second)
elif operator == "%" :
    print (first % second)
else:
    print("You enter wrong operator")

