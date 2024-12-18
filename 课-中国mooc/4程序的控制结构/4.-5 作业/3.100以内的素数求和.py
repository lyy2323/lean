# 出题说明：
# 求100以内所有素数之和并输出。
# 素数指从大于1，且仅能被1和自己整除的整数。
# 提示：可以逐一判断100以内每个数是否为素数，然后求和。

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

sum_primes = 0
for i in range(2, 100):
    if is_prime(i):
        sum_primes += i

print(sum_primes)
