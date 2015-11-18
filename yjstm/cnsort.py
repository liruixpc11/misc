# coding: utf-8 
# 中文排序样例
# Sorting Chinese Character
# henrysting@163.com
# 2009-12-25

import re

# 建立拼音辞典
dic_py = dict()
f_py = open('py.txt', "r")
content_py = f_py.read()
lines_py = content_py.split('\n')
n = len(lines_py)
for i in range(0, n - 1):
    word_py, mean_py = lines_py[i].split('\t', 1)  # 将line用\t进行分割，最多分一次变成两块，保存到word和mean中去
    dic_py[word_py] = mean_py
f_py.close()

# 建立笔画辞典
dic_bh = dict()
f_bh = open('bh.txt', "r")
content_bh = f_bh.read()
lines_bh = content_bh.split('\n')
n = len(lines_bh)
for i in range(0, n - 1):
    word_bh, mean_bh = lines_bh[i].split('\t', 1)  # 将line用\t进行分割，最多分一次变成两块，保存到word和mean中去
    dic_bh[word_bh] = mean_bh
f_bh.close()


# 辞典查找函数
def search_dict(dic, uchar):
    if isinstance(uchar, str):
        uchar = unicode(uchar, 'utf-8')
    if u'\u4e00' <= uchar <= u'\u9fa5':
        value = dic.get(uchar.encode('utf-8'))
        if value is None:
            value = '*'
    else:
        value = uchar
    return value


# 比较单个字符
def comp_char_py(A, B):
    if A == B:
        return -1
    pyA = search_dict(dic_py, A)
    pyB = search_dict(dic_py, B)
    if pyA > pyB:
        return 1
    elif pyA < pyB:
        return 0
    else:
        bhA = eval(search_dict(dic_bh, A))
        bhB = eval(search_dict(dic_bh, B))
        if bhA > bhB:
            return 1
        elif bhA < bhB:
            return 0
        else:
            return "Are you kidding?"


# 比较字符串
def comp_char(A, B):
    charA = A.decode("utf-8")
    charB = B.decode("utf-8")
    n = min(len(charA), len(charB))
    i = 0
    while i < n:
        dd = comp_char_py(charA[i], charB[i])
        if dd == -1:
            i += 1
            if i == n:
                dd = len(charA) > len(charB)
        else:
            break
    return dd


# 排序函数
def cn_sort(nline):
    n = len(nline)
    lines = "\n".join(nline)
    for i in range(1, n):  # 插入法
        tmp = nline[i]
        j = i
        while j > 0 and comp_char(nline[j - 1], tmp):
            nline[j] = nline[j - 1]
            j -= 1
        nline[j] = tmp
    return nline
