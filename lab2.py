import math
#1
a = int(input("first leg: "))
b = int(input("second leg: "))
c = math.sqrt(a * a + b * b)
print("Answer is", c)

#2
start_time_hour = 9
start_time_minute = 0
classes = int(input("Количество занятий: "))
odd_classes = (classes//2)*5
even_classes = ((classes-1)//2)*15
minutes = classes*45 + odd_classes + even_classes
print("Занятия закончатся в", start_time_hour+minutes//60, start_time_minute+minutes%60)

#3
first_number = int(input("Первое число: "))
second_number = int(input("Второе число: "))

if first_number > second_number:
    print("1")
elif first_number < second_number:
    print("2")
else:
    print("0")


#4
first_number = int(input("Первое число: "))
second_number = int(input("Второе число: "))
third_number = int(input("Третье число: "))
max_number = first_number

if second_number > max_number:
    max_number = second_number
if third_number > max_number:
    max_number = third_number
print(max_number)

#5
first_number = int(input("Первое число: "))
second_number = int(input("Второе число: "))
third_number = int(input("Третье число: "))

if first_number == second_number == third_number:
    print("3")
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print("2")
else:
    print("0")

#6
first_number = int(input("Первое число: "))
second_number = int(input("Второе число: "))
third_number = int(input("Третье число: "))
# 3 2 1
# 2 3 1
# 2 1 3
# 1 2 3
if first_number > second_number:
    first_number, second_number = second_number, first_number
if second_number > third_number:
    second_number, third_number = third_number, second_number
if first_number > second_number:
    first_number, second_number = second_number, first_number

print(first_number, second_number, third_number)

#7
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

# ax^2 + bx + c
D = b*b - 4*a*c
if D > 0:
    print((-b + math.sqrt(D))/(2*a), (-b - math.sqrt(D))/(2*a))
elif D == 0:
    print(-b/2*a)
else:
    print("No root")