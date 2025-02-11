""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """


""" temp = 67
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
    
#Challenge
""" x = input("sentence:")
y=x.split()
count = len(y)
print(count) """

#Even or Odd
""" number = int(input('enter a number:'))
if number%2 == 1:
    print('odd')
else:
    print('even') """

#Tip Calculator
""" bill = int(input('enter the bill:'))
service = input('how was the service?')
if service == 'great':
    x = bill*1.25
    print(x)
elif service == 'good':
    y = bill*1.20
    print(y)
elif service == 'okay':
    z = bill*1.15
    print(z)
elif service == 'bad':
    print(bill) """

#MADLIB
""" a = input("Select a name:")
b = input("Select a (past tense) verb:")
f = input("Select a (past tense) verb2:")
g = input("Select a number:")
c = input("Select a place:")
h = input("Select a noun:")
d = input("Select a celebrity:")
e = input("Say a compliment:")

Madlib = print(f"{a,"was walking", "to", c, "then", a, f,g, h, "and ran into", d,  "who said you're", e, "then", a, b, d}")
print(Madlib) """

#Determine Factor
""" number = int(input('enter a number:'))
for i in range(1, number+1):
    if number %i == 0:
        print(i) """

#Determine GCF
number = int(input('enter a number:'))
number2 = int(input('enter a number:'))
gcf = 1
for i  in range(1, min(number,number2)+1):
    if number%i == 0 and number2%i == 0:
        gcf = i
print(gcf)