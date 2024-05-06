n = int(input())
tiangans = ['jia','yi','bing','ding','wu','ji','geng','xin','ren','gui']
dizhis = ['zi','chou','yin','mao','chen','si','wu','wei','shen','you','xu','hai']
# 0年是 gengshen年
dis = n % 60
tiangan_dis = dis % 10
dizhi_dis = dis % 12
print(tiangans[(6+tiangan_dis)%10],dizhis[(8+dizhi_dis)%12],sep="")
