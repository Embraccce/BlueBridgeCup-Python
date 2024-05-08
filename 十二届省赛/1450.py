T = int(input())
for i in range(T):
    # 本题关键是谁操纵最后一个1，若总体1的数量为奇数，谁操纵最后一个1至关重要（因为必定是一奇一偶），而操纵这最后一个1之前的局面是两奇或两偶，不管怎么样都对自己有利。
    # 若总体1的数量为偶数，则可能会是(一奇一偶+两偶)，谁操纵最后一个1都是平局。
    nums = list(map(int,input().split()))
    nums = nums[1:]
    max_len = max(max(nums).bit_length(),1)
    b = [bin(num)[2:].zfill(max_len) for num in nums]
    count_1s = [0]*max_len
    count_0s = [0]*max_len
    for num in b:
        for i, bit in enumerate(num):
            if bit == '1':
                count_1s[i] += 1
            else:
                count_0s[i] += 1
    for idx in range(max_len):
        if count_1s[idx] == 1:
            # Alice必胜
            print(1)
            break
        elif count_1s[idx] % 2 == 0:
            # 平局
            continue
        else:
            if count_1s[idx] % 2 == 1:
                # 有奇数个1
                if count_0s[idx] % 2 == 0:
                # 若有偶数个0，Alice必胜：先选1，若对方用0跳过回合，自己也用跳过回合(0是偶数)，这样手中已经有一个1。而场面上有偶数个1，
                # Alice总可以操控最后一个1来控制输赢（因为除去手头上的最后一个1，场面上的1的数量是偶数。若自己为偶数，把1给自己；若自己为奇数，说明对方也是奇数，则把1给对方）
                    print(1)
                else:
                # 若有奇数个0，Alice必输：若先选1，则对方用0跳过回合，此时场面上还有偶数个0(用掉了一个0跳过一个回合)，所以会轮到面对偶数个1的情况，这样最后一个1被Bob操纵，自己必输。
                # 若先选0，则对方选1，此时场面上还有偶数个0，所以Alice还是要面对偶数个1的情况，这样最后一个1被Bob操纵，自己必输。
                    print(-1)
                break
    else:
        print(0)
