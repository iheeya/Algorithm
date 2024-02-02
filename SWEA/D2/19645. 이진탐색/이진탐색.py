def binary_search(P, page):
    start = 1  # 구간 초기화
    end = P
    count = 1

    while start <= end:  # 검색 구간이 유효하면 반복
        middle = (start + end) // 2  # 중앙원소 인덱스
        if middle == page:  # 배열의 중앙 값이 찾는 값과 같다면    (검색 성공)
            # count += 1  # 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
            return count

        # 중앙값이 키보다 크면
        elif middle > page:
            end = middle  # 구간을 다시 정하기
            count += 1


        else:  # 중강값이 키보다 작으면
            start = middle  # 구간 다시 정하기   // 이 과정에서는 return 값이 필요 없음 구간만 다시 정하고 while문으로 인해 위로 올라가서 다시 찾을거임
            count += 1


T = int(input())

# 중간값 포함해서 자르기. 이긴 사람 출력, 비긴 경우는 0
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    # P: 총 페이지
    # Pa: A가 찾을 페이지
    # Pb: B가 찾을 페이지
    win = None

    if binary_search(P, Pa) == binary_search(P, Pb):
        win = '0'

    elif binary_search(P, Pa) > binary_search(P, Pb):
        win = 'B'

    else:
        win = 'A'

    print(f'#{test_case} {win}')