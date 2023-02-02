# Q2 Answer template

N = input()

count = 0

n = int(N)
while(True):
    c = (n//10) + (n%10)
    n = ((n%10) * 10) + (c % 10)
    count += 1
    if int(N) == n:
        break

print(count)
