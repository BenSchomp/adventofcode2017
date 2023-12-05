
part_one = part_two = 0

file = open('day-02.txt', 'r')
for line in file:
  line = line.strip()
  values = line.split()

  # --- part one --- #

  vMin = vMax = int(values[0])
  for v in values:
    v = int(v)
    if v > vMax:
      vMax = v
    if v < vMin:
      vMin = v

  part_one += vMax - vMin

  # --- part two --- #

  for i in range(len(values)):
    for j in range(len(values)):
      if i == j:
        continue
      if int(values[i]) % int(values[j]) == 0:
        part_two += int(values[i]) / int(values[j])

file.close()

print( "part_one:", part_one )
print( "part_two:", int(part_two) )
