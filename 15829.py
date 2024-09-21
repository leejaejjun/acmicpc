def letter_to_number(letter):
    return ord(letter) - ord('a') + 1

n = int(input())
N = input()

count = 0

for i in range(n):
    count += (31**i) * letter_to_number(N[i])
    
print(count%1234567891)