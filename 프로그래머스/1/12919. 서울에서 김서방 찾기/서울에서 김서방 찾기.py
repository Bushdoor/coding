def solution(seoul):
    index= 0
    while index< len(seoul):
        if seoul[index]!= "Kim":
            index+=1
        else:
            break
    answer = f"김서방은 {index}에 있다"
    return answer