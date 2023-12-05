
part_one = part_two = 0

file = open('day-02.txt', 'r')
for line in file:
  line = line.strip()
  values = line.split()

  vMin = vMax = int(values[0])
  for v in values:
    v = int(v)
    if v > vMax:
      vMax = v
    if v < vMin:
      vMin = v
  checksum = vMax - vMin
  part_one += vMax - vMin
  print( line, ':', checksum )

file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )
