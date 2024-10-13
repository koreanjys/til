def solution(k, room_number):
    answer = []

    next = {}
    for num in room_number:
        _num = num
        visit = [_num]
        while _num in next:
            _num = next[_num]
            visit.append(_num)
        answer.append(_num)
                
        next_num = _num + 1
        while next_num in next:
            next_num += 1
        
        for num in visit:
            next[num] = next_num
    
    return answer