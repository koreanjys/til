def solution(text, anagram, sw):
    if sw == True:
        new_text = []
        for idx, n in enumerate(anagram):
            new_text.append((n, text[idx]))
        new_text.sort()
        new_text = ''.join(list(map(lambda char: char[1], new_text)))
        return new_text
    else:
        new_text = []
        for idx, n in enumerate(anagram):
            new_text.append((idx, text[n]))
        new_text.sort()
        new_text = ''.join(list(map(lambda char: char[1], new_text)))
        return new_text

print(solution('Hello', [4, 2, 0, 1, 3], True))  # 'lleoH'
print(solution('lleoH', [4, 2, 0, 1, 3], False))  # 'Hello'