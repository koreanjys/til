import sys
sys.stdin = open('input.txt')

# 비트연산 xor 사용(0과 1이 다르니까 1이됨, 1과 1이 같으니까 0이됨)   예시) 0^1 >> 1   1^1 >> 0

sw_ea = int(input())  # 스위치 갯수 # 8
sw_statuses = [8] + list(map(int, input().split())) + [9]  # 스위치 상태들 # [8, 0, 1, 0, 1, 0, 0, 0, 1, 9]  8, 9는 쓰지않는 인덱스 0번 과 끝번
end_idx = len(sw_statuses) - 2
students = int(input())  # 학생 수 2
fm_nums = []
for student in range(students):
    fm_nums.append(list(map(int,(input().split()))))  # [성별, 번호] 리스트를 저장

for fm in fm_nums:

    if fm[0] == 1:  # 성별이 남성이면
        for idx in range(1, end_idx + 1):
            if idx % fm[1] == 0:  # 배수이면
                sw_statuses[idx] ^= 1
    elif fm[0] == 2:  # 성별이 여자면
        n = 1
        idx = fm[1]
        sw_statuses[idx] ^= 1
        while sw_statuses[idx-n] == sw_statuses[idx+1]:
            sw_statuses[idx-n] ^= 1
            sw_statuses[idx+n] ^= 1
            n += 1
answer = ' '.join(list(map(str, sw_statuses[1:end_idx + 1])))
print(answer)