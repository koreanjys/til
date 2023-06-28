def solution(queries):
    
    
    # 마지막 n세대
    n = sorted(queries)[-1][0]
    
    # 리스트
    p_list = ['Rr' for _ in range(n)]

    # 세대 증식
    for i in range(1, n):
        # 1세대부터 n세대 까지 (index_0 은 1세대)
        
        # 홀수 세대는 Rr 짝수 세대는 Tt
        # i는 인덱스라 0부터 시작, 고로 i 짝수가 곧 홀수
        if i % 2 == 1:  # 짝수세대
            p_list[i] = p_list[i-1].replace('RR', 'TT'*4).replace('Rr', 'TTTtTttt').replace('rr', 'tt'*4)
        else:
            p_list[i] = p_list[i-1].replace('TT', 'RR'*4).replace('Tt', 'RRRrRrrr').replace('tt', 'rr'*4)
    
    answer = []
    for n, p in queries:
        if n == 1:
            char = 'Rr'
        else:
            char = p_list[n-1][p*2-2:p*2]
            char = char.replace('T', 'R').replace('t', 'r')
        answer.append(char)
    return answer

print(solution([[16, 2]]))
        
                    
                    
                    
                
        
        
        
        
        
        