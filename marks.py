
n = int(input("Number of subs: "))

result = []
print("credits grade: example 1 a")
credit = dict()
for i in range(n):
    score = input().split()
    credit[int(score[0])] = score[1]

reference = [chr(i) for i in range(97,103)]
reference_mark = list(range(9,0,-2))


total_credits = sum(credit.keys())

plus = False

for k, v in credit.items():

    value = v.lower()

    if len(value) == 2:
        plus = True
    else:
        plus = False

    for i in reference:
        if value[0] == i:
            index = reference.index(i)
            break

    temp_score = k*reference_mark[index]

    if plus:
        temp_score+=1

    result.append(temp_score)
        
sgpa = sum(result)/total_credits

print(sgpa)



