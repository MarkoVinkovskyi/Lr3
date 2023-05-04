n = int(input())
a = list(map(int, input().split()))

min_idx = a.index(min(a))
max_idx = a.index(max(a))

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

count_zeros = 0
for i in range(min_idx, max_idx + 1):
    if a[i] == 0:
        count_zeros += 1

print(count_zeros)
