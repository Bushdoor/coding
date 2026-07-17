def solution(a, b):
    answer = 0
    if int(f"{a}{b}")> 2*a*b:
        answer= int(f"{a}{b}")
    elif int(f"{a}{b}")< 2*a*b:
        answer= 2*a*b
    else:
        answer= int(f"{a}{b}")
    return answer