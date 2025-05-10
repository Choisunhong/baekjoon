import sys
input = sys.stdin.readline

def solution(array, commands):
    answer =[]
    for command  in commands:
        i,j,k = command
        sub = sorted(array[i-1:j])
        answer.append(sub[k-1])
    return answer