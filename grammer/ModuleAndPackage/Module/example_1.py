"""2値の最小値と最大値を求める"""

def min_max2(a, b):
    return (a, b) if a < b else (b, a)

n1 = int(input('Integer 1:'))
n2 = int(input('Integer 2:'))

minimum, maximum = min_max2(n1, n2)
print('min = ', minimum, ' and max = ', maximum)