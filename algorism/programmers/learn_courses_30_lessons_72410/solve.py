import re

def solution(new_id):
    
    # 1단계 => 소문자
    new_id = new_id.lower()
    
    # 2단계 => 특수문자 제거
    new_id = re.sub(r"[^-_.0-9a-zA-Z]", "", new_id)
    
    # 3단계 마침표(.)가 2번 이상 연속일 경우 마침표 한개로
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계 마침표 처음 끝 제거
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5단계 빈 문자열 a 대입
    new_id = new_id.replace(' ', 'a')
    
    # 6단계 길이 제한
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        
    # 7단계 최소 길이
    while 3 > len(new_id):
        if len(new_id) == 0:
            new_id = 'a'
        else:
            new_id = new_id + new_id[-1]
    
    return new_id
            
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))