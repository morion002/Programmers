def solution(array, commands):
    answer = []
    for q in range(len(commands)):
        i, j, k = commands[q][0], commands[q][1], commands[q][2]
        temp = []
        for p in range(i-1, j):
            temp.append(array[p])
        temp.sort()
        answer.append(temp[k-1])
    return answer
