T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    result = A+B
    
    print(f'Case #{tc}: {A} + {B} = {result}')