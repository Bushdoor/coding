def solution(a, d, included):
    answer = 0
    
    for i in range(0, len(included), 1):
        if included[i]== True:
            answer+= a+ i* d
            
    return answer