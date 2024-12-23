while(True):
    try:
       n = int(input())  # 입력값 n
    except:
        break
    
    i = 0  # 자릿수를 카운트할 변수
    num = 0  # 배수

    while(True):
        num = (num * 10) + 1
        i += 1

        if (num % n == 0):
            print(i)
            break
         

