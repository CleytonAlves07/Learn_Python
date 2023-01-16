file = 'pythontxt.txt'

with open(file) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line)