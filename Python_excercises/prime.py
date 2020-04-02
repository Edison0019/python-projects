def is_prime(n):
    if n < 2 or n == 2:
        return True
    else:
        x = 2
        while x < n:
            if n % x == 0:
                return False
            x += 1
        return True

print(is_prime(2))