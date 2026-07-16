def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(0, 5, 1):
            if action == basic_order[i]:
                answer.append(basic_order.index(action)+1)
    return answer
