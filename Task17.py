n = int(input())
a = list(map(int, input().split()))
def sort_key(x):
    return (abs(x), -x)
a = sorted(a, key=sort_key)
print(*a)
