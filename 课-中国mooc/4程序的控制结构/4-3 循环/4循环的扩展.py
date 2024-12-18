for c in 'python':
    if c == 't':
        continue
    print(c, end='')
else:
    print('\n'+'这段文字的正常出现，表示没有遇到break终止')

for c in 'python':
    if c == 't':
        break
    print(c, end='')
else:
    print('\n'+'这段文字没有出现，所以中途是遇到了break的终止')