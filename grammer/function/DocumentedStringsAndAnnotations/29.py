"""アノテーションと文書化文字列付き関数"""

def puts(n: int, s: str) -> None:
    """n個のsを連続して表示

    仮引数:
        n -- 表示する文字列の個数
        s -- 表示する文字列
    返却値:
        無し
    
    """
    for _ in range(n):
        print(s, end='')


print(puts.__doc__)