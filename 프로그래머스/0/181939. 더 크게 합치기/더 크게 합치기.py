def solution(a, b):
    answer = ''
    if f"{a}{b}"> f"{b}{a}":
        answer= int(f"{a}{b}")
    elif f"{a}{b}"< f"{b}{a}":
        answer= int(f"{b}{a}")
    else:
        answer= int(f"{a}{b}")
    return answer