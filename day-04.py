
part_one = part_two = 0

file = open('day-04.txt', 'r')
for line in file:
  found_duplicate = False
  phrases = set()
  line = line.strip()
  words = line.split()
  for w in words:
    if w in phrases:
      found_duplicate = True
      break
    else:
      phrases.add(w)

  if not found_duplicate:
    part_one += 1

file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )
