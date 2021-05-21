"Сумму цифр  рекурсией"
def power(n):
    sum = 0
    while n>=1:

print(power(12345))





exit()
"""Дано натуральное число n. Вывести все числа от 1 до n"""
def power(n, start):
    if start > n:
        return 0
    print(start)
    return power(n, start +1)


print(power(10,0))



exit()
def fibonachi2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi2(n-1) + fibonachi2(n-2)

print(fibonachi2(6))

for i in range(10):
    print(fibonachi2(i))




exit()
def fibonachi(a, limit):
    if len (a) > limit:
        return a
    a.append(a[-1] + a[-2])
    return fibonachi(a, limit)





print(fibonachi(2))



exit()
def power(x):
    x[0] = 10
    return x

my_list = [1,2,3]
print(power(my_list))
print(my_list)

my_str = "123"
print(power(my_str))



exit()
def my_append(my_list, obj):
    m = [0]
    result = my_list + m
    result[-1] = obj
    return result


my_list_new = [1, 2, 3, 4, 5]

print(my_append(my_list_new, True))
