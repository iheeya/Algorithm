S = input()

result = [0]*26   # 알파벳의 개수를 저장할 리스트

for s in S:
    result[ord(s)-97] += 1

for i in range(len(result)):
    print(result[i], end = ' ')
