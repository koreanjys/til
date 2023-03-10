def solution(data):
	
    # 10진수 담을 빈 리스트 생성
    new_data = []
    
    # +는1, -는0 바꿈 => 정수로 변환 => 아스키코드로 변환
    for d in data:
        d = d.replace('+', '1')
        d = d.replace('-', '0')
        d = d.strip()
        print(d)
        # new_data.append(chr(int(d.strip)))
        
	# 마지막 전처리 리스트를 str로 변경
    return ''.join(new_data)


data = [' + - - + - + - ', ' + + + - + - + ', ' + + - + + + - ']

print(solution(data))