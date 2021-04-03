n = int(input())
phoneBook = dict(input().split() for _ in range(n))
    
for i in range(0, n):
    name = input()
    if name in phoneBook:
        print(f'{name}={str(phoneBook[name])}')
    else:
        print("Not found")