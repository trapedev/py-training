"""最小値と最大値を求めるモジュール"""

def min_max2(a: int, b: int) -> int:
    """aとbの最小値と最大値を求めて返却"""
    return min(a, b), max(a, b)

def min_max3(a: int, b: int, c: int) -> int:
    """aとbとcの最小値と最大値を求めて返却"""
    return min(a, b, c), max(a, b, c)

if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    z = int(input('z = '))

    print('min(x, y) = {}, max(x, y) = {}'.format(*min_max2(x, y)))
    print('min(y, z) = {}, max(y, z) = {}'.format(*min_max2(y, z)))
    print('min(z, x) = {}, max(z, x) = {}'.format(*min_max2(z, x)))
    print('min(x, y, z) = {}, max(x, y, z) = {}'.format(*min_max3(x, y, z)))