
file = open('day-01.txt', 'r')
for line in file:
  part_one = part_two = 0
  line = line.strip()
  n = len(line)

  i = 0
  while i < n-1:
    if line[i] == line[i+1]:
      part_one += int(line[i])
    if line[i] == line[int((i+(n/2))%n)]:
      part_two += int(line[i])
    i += 1

  if line[n-1] == line[0]:
    part_one += int(line[0])

file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )
