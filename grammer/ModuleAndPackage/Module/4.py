"""example_2モジュールの関数群を呼び出す"""

import example_2

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

print('min(x, y) = {}, max(x, y) = {}'.format(*example_2.min_max2(x, y)))
print('min(y, z) = {}, max(y, z) = {}'.format(*example_2.min_max2(y, z)))
print('min(z, x) = {}, max(z, x) = {}'.format(*example_2.min_max2(z, x)))
print('min(x, y, z) = {}, max(x, y, z) = {}'.format(*example_2.min_max3(x, y, z)))