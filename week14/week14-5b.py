#SOIT106_ADVANCE_012
a = list(map(int, input().split()))

ans = 0
N = len(a)
for i in range(N-2):
    if a[i] == a[-1]:
        ans +=1
    
print(ans)