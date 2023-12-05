
n = 368078
x = y = 0
multiplier = xm = ym = 1
delta = 1
values = {'0,0': 1}
part_one = part_two = None

def getKey(a,b):
  return ("%i,%i" % (a,b))

def getNeighborSum(a,b):
  sum = 0
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      if dx == 0 and dy ==0:
        continue

      k = getKey(a+dx, b+dy)
      if k in values:
        sum += values[k]

  return sum

i = 1
while i < n:
  i += 1
  if xm > 0:
    x += delta
    xm -= 1
  elif ym > 0:
    y += delta
    ym -= 1

    if ym == 0:
      multiplier += 1
      xm = ym = multiplier
      delta *= -1

  if not part_two:
    nSum = getNeighborSum(x,y)
    values[getKey(x,y)] = nSum 

    if nSum > n:
      part_two = nSum

print( "%d: (%d, %d)" % (i, x, y) )
part_one = abs(x) + abs(y)

print( "part_one:", part_one )
print( "part_two:", part_two )
