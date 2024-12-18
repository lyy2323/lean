steps = 0
def move(n,a,b,c):
    global steps
    if n == 1:
        steps += 1
        print('step{:>4} move{}->{}'.format(steps,a,c))
    else:
        move(n-1,a,c,b)
        steps += 1
        print('step{:>4} move{}->{}'.format(steps, a, c))
        move(n-1,b,a,c)
move(3,'A','B','C')

