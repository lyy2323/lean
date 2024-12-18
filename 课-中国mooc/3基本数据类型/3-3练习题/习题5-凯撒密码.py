s = input()
t = ''
for i in s:
    if 'a' <= i <= 'z':
        t += chr( ord('a') + ((ord(i)-ord('a')) + 3)%26 )
    elif 'A' <= i <= 'Z':
        t += chr( ord('A') + ((ord(i)- ord('A')) + 3)%26 )
    else:
        t += i
print(t)