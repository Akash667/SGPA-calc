
n = int(input("Number of subs: "))

result = []
print("credits grade: example 1 a")
credit = dict()
for i in range(n):
    score = input().split()
    credit[int(score[0])] = score[1]


total_credits = sum(credit.keys())

plus = False

for k, v in credit.items():

    value = v.lower()

    if len(value) == 2:
        plus = True
    else:
        plus = False

    difference = ord(value[0])  - ord("a")

    temp_score = 10 - difference

    if not plus:
        temp_score-=1

    result.append(temp_score*k)
        
sgpa = sum(result)/total_credits

print(sgpa)



