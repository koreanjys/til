https://school.programmers.co.kr/learn/courses/30/lessons/12973#

def solution(s):
    answer = -1
    """
    while 1 < len(s):
        s_len = len(s)
        new_s = list(s)
        for i in range(s_len - 1):
            if new_s[i] != "" and new_s[i] == new_s[i + 1]:
                new_s[i] = ""
                new_s[i + 1] = ""
        
        s = "".join(new_s)
        
        if s_len == len(s):
            break
    return 1 if len(s) == 0 else 0
    """
    ##################################
    """
    while 1 < len(s):
        s_len = len(s)
        new_s = list(s)
        for i in range(s_len - 1):
            if new_s[i] != "" and new_s[i] == new_s[i + 1]:
                extend = 0
                while new_s[i - extend] != "" and \
                    0 <= i - extend and i + extend + 1 < s_len and \
                    new_s[i - extend] == new_s[i + extend + 1]:
                    new_s[i - extend] = new_s[i + extend + 1] = ""
                    extend += 1
        
        s = "".join(new_s)
        
        if s_len == len(s):
            break
    return 1 if len(s) == 0 else 0
    """
    #################################
    """
    dict = {}
    s = list(s)
    for i in range(len(s)):
        c = s[i]
        if c not in dict:
            dict[c] = 0
        dict[c] += 1 if i % 2 == 0 else -1

    return 0 if any(dict.values()) else 1
    """
    ####################################
    stack = []
    for c in s:
        if 0 < len(stack) and stack[-1] == c:
            stack.pop()
        else :
            stack.append(c)
    s = "".join(stack)
    return 1 if len(s) == 0 else 0