'''
외톨이 알파벳 = 2회 이상 2부분

'''
def solution(input_string):
    answer = ''
    
    dic = {}
    
    for idx, st in enumerate(input_string):
        
        dic[st] = 0
        
        if idx > 0:
            if st == input_string[idx - 1]:
                pass
            else:
                dic[st] += 1
                
        # 첫 인덱스 문자열은 cnt + 1
        else:
            dic[st] += 1
        
        # 외톨이 문자를 알파벳 순으로
        answer = list(filter(lambda x: dic[x] > 1))
        if answer:
            answer.sort(reverse=True)
            answer = ''.join(answer)
        else:
            answer = "N"
    return answer