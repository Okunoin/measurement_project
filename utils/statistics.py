def calculate_average(num):
    sm = 0
    for i in num:
        sm+=i
    return sm/len(num)
def find_min(num):
    mn = num[0]
    for i in num:
        if mn>i:
            mn=i
    return mn
def find_max(num):
    mx = num[0]
    for i in num:
        if mx<i:
            mx = i
    return mx