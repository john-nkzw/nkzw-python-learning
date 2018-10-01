num = int(input().rstrip())
result = [str(num * i) for i in range(1, 10)]
print(' '.join(result))
