# アノテーション付きの関数puts

def puts(n: int, s: str)-> None: 
    # (n: int, s: str) 仮引数に対するアノテーション
    # -> None 返却値に対するアノテーション
    """n個のsを連続して表示"""
    for _ in range(n):
        print(s, end='')

puts(5, '*')
print()
print(puts.__annotations__) # アノテーションの各項目の内容を辞書化したものは、関数名.__annotations__で取り出せる。
print()