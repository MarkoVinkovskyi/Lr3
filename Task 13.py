n = int(input())
a = list(map(int, input().split()))

min_elem = min(a)
next_min_elem = float('inf')
next_min_index = -1

for i in range(n):
    if a[i] > min_elem and a[i] < next_min_elem:
        next_min_elem = a[i]
        next_min_index = i

print(next_min_elem, next_min_index+1)
