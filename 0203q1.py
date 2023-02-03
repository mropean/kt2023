# Q1 Answer template

def solution(lottos, win_nums):
    answer = []
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
            
    z_count = lottos.count(0)
    
    # 최대
    max_lotto = count + z_count
    if max_lotto == 6:
        answer.append(1)
    elif max_lotto == 5:
        answer.append(2)
    elif max_lotto == 4:
        answer.append(3)
    elif max_lotto == 3:
        answer.append(4)
    elif max_lotto == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    # 최소
    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)
