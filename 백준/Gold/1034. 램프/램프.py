from collections import defaultdict

N,M = map(int,input().split())
lamp = []

for _ in range(N):
    lamp.append(input())

K = int(input())
d = {}

for i in lamp:
    if d.get(i):
        d[i][0]+=1
    else:
        #존재 안하면 "01" : [총 개수, 0의 수 ]
        cnt = i.count("0")
        d[i] = [1,cnt]

result = []
for i in d.values():
    result.append(i)

result.sort(reverse=True)
answer = 0
for i in range(len(result)):
    light_num,zero = result[i]

    if K < zero:
        continue
    else:
        if (K - zero)%2 == 0:
            # print("light_num,zero : ",light_num,zero)
            answer = light_num
            break;
        else:
            continue
print(answer)