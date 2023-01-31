a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if c <= b <= a:
    a, b, c = c, b, a
elif b <= c <= a:
    a, b, c = b, c, a
elif c <= a <= b:
    a, b, c = c, a, b
elif a <= c <= b:
    a, b, c = a, c, b
elif a <= b <= c:
    a, b, c = a, b, c
elif b <= a <= c:
    a, b, c = b, a, c
if d <= e:
    d, e = d, e
elif e <= d:
    d, e = e, d
if a <= d and b <= e:
    print('YES')
else:
    print('NO')
