n = int(input())
a = input().split()

# функция для вычисления суммы цифр числа
def digit_sum(num):
    return sum(int(d) for d in str(abs(num)))

# вычисляем сумму цифр для каждого числа и сохраняем в словаре
digit_sums = {}
for num in a:
    if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
        digit_sums[int(num)] = digit_sum(int(num))

# находим элементы с минимальной и максимальной суммой цифр
min_digit_sum = min(digit_sums.values())
max_digit_sum = max(digit_sums.values())
min_element = min(k for k, v in digit_sums.items() if v == min_digit_sum)
max_element = max(k for k, v in digit_sums.items() if v == max_digit_sum)

# выводим результаты
print(min_element)
print(max_element)
