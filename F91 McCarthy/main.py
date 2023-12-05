def f91(n):
    if n <= 100:
        return f91(f91(n+11))
    return n - 10

while N := int(input()):
    print(f'f91({N}) = {f91(N)}')