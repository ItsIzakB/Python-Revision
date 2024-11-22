
import time
#priting
#
# hello = 'tim'
#
# world = 'world'
#
# hello = 'hello'

# print(hello, world)

# input
#
# input =input()
#
# print (input)

#typecasting

# integer = 12
#
# intToFloat = float(integer)
#
# word = 45
#
# wordToInt = int(word)
#
# word += 5
#
# print(word)
#
# print(type(word))

for i in reversed(range(6)):
    print(i)
    time.sleep(1)
print("boo")

#alt sol:

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("boo")
time.sleep(1)
print("again...")

#List

employees = ['john', 'joe', 'jake']
print(employees)

employees.append("jaqiem")
employees.remove("john")
employees.pop(1)
for employee in employees:
    print(employee)



