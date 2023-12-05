
file = open('day-01.txt', 'r')
for line in file:
  part_one = part_two = 0
  line = line.strip()

  i = 0
  n = len(line)
  while i < n:
    if line[i] == line[int(i+1)%n]:
      part_one += int(line[i])
    if line[i] == line[int((i+(n/2))%n)]:
      part_two += int(line[i])
    i += 1

file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )
