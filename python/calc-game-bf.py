# Brute Forcing Calc Game lvl 118
# 2152 -> 13
# Keys: 'a' 25=>12, 'b' 21=>3, 'c' 12=>5, 'd' Shift>, 'e' Reverse
# 5 keys, 6 moves. 15625 possibilities. And 2 hours before bedtime.
# Can't find a solution by hand. Lets bruteforce this.

import re

def rshift(n):
    return n[-1]+n[:-1]

def bt(moves, n, p):
    if n == '13':
        print('WIN:', p, n)
        return (n, p)
    if moves is 0:
        print('END:', p, n)
        return None
    a = bt(moves-1,re.sub('25','12',n),p+'a')
    if a:
        return a
    b = bt(moves-1,re.sub('21','3',n),p+'b')
    if b:
        return b
    c = bt(moves-1,re.sub('12','5',n),p+'c')
    if c:
        return c
    d = bt(moves-1,rshift(n),p+'d')
    if d:
        return d
    e = bt(moves-1,n[::-1],p+'e')
    if e:
        return e

if __name__ == '__main__':
    print(bt(6,'2152',''))
