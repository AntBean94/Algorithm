# BOJ 17609 회문

def is_palindrome(char, l, r):
    while l <= r:
        if char[l] == char[r]:
            l += 1
            r -= 1
        else:
            return [l + 1, r, l, r - 1]
    return False

T = int(input())
for tc in range(T):
    char = input()
    l, r = 0, len(char) - 1
    info = is_palindrome(char, l, r)
    if info:
        l1, r1, l2, r2 = info
        info1 = is_palindrome(char, l1, r1)
        info2 = is_palindrome(char, l2, r2)
        if not (info1 and info2): print(1)
        else: print(2)
    else:
        print(0)

'''
2
abbab
abcddadca

1
2
'''