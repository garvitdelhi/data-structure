__author__ = 'garvit'

import time;


def check_anagram(w1, w2):
    w1 = list(w1)
    s = time.time()
    if len(w1) != len(w2):
        e = time.time()
        return False, e-s
    for i in w2:
        if i not in w1:
            e = time.time()
            return False, e-s
        else:
            w1.remove(i)
    e = time.time()
    return True, e-s

print(check_anagram('abcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad','dcbacabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad'))


def anagramSolution1(s1,s2):
    s = time.time()
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    e = time.time()
    return stillOK, e-s

print(anagramSolution1('abcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad','dcbacabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad'))

def anagramSolution2(s1,s2):
    s = time.time()
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    e = time.time()
    return matches, e-s

print(anagramSolution2('abcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad','dcbacabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad'))

def anagramSolution4(s1,s2):
    s = time.time()
    s = time.time()
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    e = time.time()
    return stillOK, e-s

print(anagramSolution4('abcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad','dcbacabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcadabcad'))