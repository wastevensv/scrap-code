# Originally found on johnroach.io. Modified for absolute location relative to starting position.
mouse = open('/dev/input/mouse1', 'rb')

def to_signed(n):
    return n - ((0x80 & n) << 1)

x = 0
y = 0

while True:
    status, dx,dy = tuple(c for c in mouse.read(3))
    x += to_signed(dx)
    y += to_signed(dy)
    print("%#02x %d %d" % (status, x, y))
