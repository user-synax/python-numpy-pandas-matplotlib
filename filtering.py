import numpy as np

ages = np.array([[25, 17, 35, 16, 45], [50, 25, 21, 65, 20]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
print(teenagers)
print(adults)
print(seniors)

adults2 = np.where(ages >= 18, ages, 'Not matched')
print(adults2)

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

evens = numbers[numbers % 2 == 0]
print(evens)
odds = numbers[numbers % 2 != 0]
print(odds)