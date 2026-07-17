def solution(num_list):
    answer = 0
    mul= 1
    sum1= 0
    for i in num_list:
        mul*= i
        sum1+= i
        
    if mul< (sum1* sum1):
        answer= 1
    else:
        answer= 0
        
    return answer