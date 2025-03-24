import bisect

def generate_lucky_numbers(number, fours, sevens, lucky):
    if number > 1e10:
        return
    
    if fours == sevens:
        lucky.append(number)
    
    generate_lucky_numbers(number * 10 + 7, fours, sevens + 1, lucky)
    generate_lucky_numbers(number * 10 + 4, fours + 1, sevens, lucky)

lucky = []
generate_lucky_numbers(4, 1, 0, lucky)
generate_lucky_numbers(7, 0, 1, lucky)

lucky.sort()

n = int(input())
index = bisect.bisect_left(lucky, n)
print(lucky[index])
