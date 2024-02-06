A = []

for row in range(0,9):
  row = list(map(int, input().split()))
  A.append(row)

big = 0

for row in range(0,9):
  for col in range(0,9):
    if A[row][col] >= big:
      big = A[row][col]
      r=row
      c=col

print(big)
print(r+1 ,c+1)

    


