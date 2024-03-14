numbers = list(range(0, 101))

oddNumbers = [number for number in numbers if number % 2 != 0]
print(oddNumbers)

evenNumbers = [number for number in numbers if number % 2 == 0]
print(evenNumbers)

for number in numbers:
    m_3 = [number * 3]
    print(f'result : {m_3}')


# fixed this above :)
# page 60