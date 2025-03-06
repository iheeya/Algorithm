N = int(input())   # 과목의 개수
score = list(map(float, input().split()))   # 과목의 점수를 공백을 기준으로 리스트에 저장

# 최고점을 기준으로 새로운 성적 만들기

# 최고점 구하기
highest = max(score)

# 새로운 성적을 만드는 식
new_score = [0] * N

for i in range(len(score)):
    new_score[i] = score[i]/highest*100

print(sum(new_score)/N)