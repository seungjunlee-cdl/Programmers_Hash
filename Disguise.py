Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(clothes):
    answer=1
    set_clothes = []
    clothes_dict = {}
    
    for i in clothes:
        set_clothes.append(i[1])
    set_clothes = set(set_clothes)

    for i in range(len(set_clothes)):
        clothes_dict[list(set_clothes)[i]] = 0

    for i in clothes:
        clothes_dict[i[1]] += 1

    for i in clothes_dict.values():
        answer *= (i+1)
    answer -= 1
    
    return answer