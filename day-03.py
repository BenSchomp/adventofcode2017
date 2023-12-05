
n = 368078
x = y = 0
multiplier = xm = ym = 1
delta = 1

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

print( "%d: (%d, %d)" % (i, x, y) )
part_one = abs(x) + abs(y)

print( "part_one:", part_one )
