number = 5
result = 1

for num in range(1, number+1):
  result *= num
print(result)


ratings = [6, 8, 5, 9, 10]

new_ratings = [rating*10 for rating in ratings]

print(new_ratings)