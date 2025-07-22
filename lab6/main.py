grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(filter(lambda x: x >= 60, grades))
passed_with_bonus = list(map(lambda x: x * 1.05, passed_with_bonus))
print(passed_with_bonus)