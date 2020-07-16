result = []
credit = []


file_handle = open("marks_list.txt")

lines = file_handle.readlines()

n = len(lines)


for i in lines:
    try:
        score = i.split()
        if score[1] == "None" or score[1] == "Qualified":
            continue
        score[0] = float(score[0])
        credit.append(score)
    except:
        n-=1
        pass

reference = [chr(i) for i in range(97,102)]

reference_mark = list(range(9,0,-2))

total_credits = sum([i[0] for i in credit])
print(total_credits)

plus = False

for k, v in credit:

    value = v.lower()

    if len(value) == 2:
        plus = True
    elif len(value) == 1:
        plus = False

    for i in reference:
        if value[0] == i:
            index = reference.index(i)
            break

    temp_score = reference_mark[index]

    if plus:
        temp_score += 1
    
    temp_score *= k

    result.append(temp_score)

print(result)

sgpa = sum(result)/total_credits

print(sgpa)



