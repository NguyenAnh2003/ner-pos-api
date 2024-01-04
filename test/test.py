
n = int(input())
n=bin(n)[2:].split("0")
max=0
for i in n:
    if len(i)> max :
        max = len(i)
print(max)