def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = []
        for p in range(i-1, j):
            temp.append(array[p])
        temp.sort()
        answer.append(temp[k-1])
    return answer
