student_num = int(input())  # 학생 수
student = [i for i in range(1, student_num+1)]  # 학생 번호

# 학생들이 뽑은 숫자만큼 앞으로 가기
flag = list(map(int, input().split()))

for i in range(student_num):
    change = i
    for _ in range(flag[i]):
        student[change], student[change-1] = student[change-1], student[change]
        change -= 1


print(*student)