# 名前修飾の確認

class C():
    __abc = 5

# 変更後の名前でアクセス可能
print(C._C__abc)

# 変更前の名前でアクセス不可能
print(C.__abc)