part_one = part_two = 0

file = open('day-01.txt', 'r')
for line in file:
  sum = 0
  line = line.strip()
  n = len(line)

  i = 0
  while i < n-1:
    if line[i] == line[i+1]:
      sum += int(line[i])

    i += 1

  if line[n-1] == line[0]:
    sum += int(line[0])

  print( line, sum )

file.close()

print( "part_one:", sum )
print( "part_two:", part_two )
