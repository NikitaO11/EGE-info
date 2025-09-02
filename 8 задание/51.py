from itertools import *

nch = '1357'
ch = '2468'
k = 0

for i in product(nch, ch, nch, ch, nch, ch, nch, ch, nch, ch, nch):
    s = ''.join(i)
    if s.count('1') <= 4 and s.count('2') <= 4 and s.count('3') <= 4 and s.count('4') <= 4 and \
       s.count('5') <= 4 and s.count('6') <= 4 and s.count('7') <= 4 and s.count('8') <= 4:
        k += 1

print(k * 2)

