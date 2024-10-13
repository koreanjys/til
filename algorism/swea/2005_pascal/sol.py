import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    layers = []
    for n in range(N):  # n 층
        if n == 0:  # 첫번째 층엔 [1] 부여
            layers.append([1])
            continue
        layer = [1] * (n + 1)
        end = len(layer)
        for idx in range(end):
            if idx == 0 or idx == end - 1:  # 현재 n 층의 처음 idx 와 끝 idx 에 값 1 부여
                layer[idx] = 1
            else:
                layer[idx] = layers[n - 1][idx - 1] + layers[n - 1][idx]  # 현재 값은 윗층 (현재 idx - 1) + (현재 idx)
        layers.append(layer)  # 만들어 진 층을 layers 에 추가
    answer = '\n'.join([' '.join(map(str, layer)) for layer in layers])  # 2차원 리스트를 문자열로 변환

    print(f'#{tc}\n{answer}')