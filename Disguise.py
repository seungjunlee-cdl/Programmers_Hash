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
