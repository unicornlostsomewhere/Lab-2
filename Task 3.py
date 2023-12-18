# Дан двумерный массив и два числа: i и j. Поменяйте в массиве
# столбцы с номерами i и j и выведите результат. Программа получает
# на вход размеры массива n и m, затем элементы массива, затем числа i и j.

def swapping(array, i, j):
    for row in array:
        row[i], row[j] = row[j], row[i]
    return array

try:
    n, m = map(int, input("Enter n and m for the array: ").split())
    array = []
    for x in range(n):
       row = []
       for y in range(m):
          numbers = int(input("Enter a number: "))
          row.append(numbers)
       array.append(row)
    for i in range(n):
          print(array[i])
    i, j = map(int, input("Enter i and j: ").split())
    if i > m or j > m or i < 0 or j < 0:
           print("Incorrect column values.")
    else:
           modified_array = swapping(array, i, j)
           print("Modified Array:")
           for row in modified_array:
                 print(row)
except ValueError:
    print("You entered a value in an incorrect format. Please restart the program. ")
except Exception:
    print("Something weird happened. Go check the code!!")
finally:
    print("The code was compiled. That's the end:)")
