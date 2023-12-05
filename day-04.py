
part_one = part_two = 0

file = open('day-04.txt', 'r')
for line in file:
  found_duplicate = False
  found_anagram = False
  phrases = set()
  anagrams = set()

  line = line.strip()
  words = line.split()

  # --- part one ---
  for w in words:
    if w in phrases:
      found_duplicate = True 
      break
    else:
      phrases.add(w)

  if not found_duplicate:
    part_one += 1

  # --- part two ---
  for w in words:
    w = ''.join(sorted(w))
    if w in anagrams:
      found_anagram = True
      break
    else:
      anagrams.add(w)

  if not found_anagram:
    part_two += 1

file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )
