T = int(input())
def b_s(right):
    l,r = -1,right+1
    while l+1!=r:
        m=l+r>>1
        if (m+1)*m//2 <= right:
            l = m
        else:
            r = m
    return l
for _ in range(T):
    li,ri = map(int,input().split())
    li -= 1
    #计算[li,ri]
    # 等价于计算sum[1,ri]-sum[1,li-1]
    # 首先要找到最接近ri的n2
    n2 = b_s(ri)
    # 继续找要找到最接近li-1的n1
    n1 = b_s(li)
    l_sum = (1+n1)*n1//2
    r_sum = (1+n2)*n2//2
    ans = 0
    ans += (n2*(n2+1)*(2*n2+1)+(3*n2*(n2+1))) // 12
    r_num = ri - r_sum
    ans += (r_num+1)*r_num//2
    ans -= (n1*(n1+1)*(2*n1+1)+(3*n1*(n1+1))) // 12
    l_num = li - l_sum
    ans -= (l_num+1)*l_num//2
    print(ans)
    
    
