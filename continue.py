# filename: continue.py

while True:
    s = input('enter something')
    if s == 'quit':
        break
    if len(s)<3:
        continue
    print('哈哈哈')

