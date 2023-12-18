def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num%i == 0:
           return False
    print("Ok")

number = int(input("Enter a number: "))
prime_number(number)
