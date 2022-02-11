Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(genres, plays):
    total_play_dict = {}
    numbers = []
    
    total_list = [[genres[i],plays[i],i] for i in range(len(genres))]
    list_sorted = sorted(total_list,key= lambda x: (-x[1],x[2]))

    for m in total_list:
        if m[0] not in total_play_dict.keys():
            total_play_dict[m[0]] = m[1]
        else:
            total_play_dict[m[0]] += m[1]

    total_play_dict = sorted(total_play_dict.items(), key = lambda x:-x[1])

    for m in total_play_dict:
        cnt = 0
        for l in list_sorted:
            if m[0] == l[0]:
                cnt += 1
                if cnt <= 2:
                    numbers.append(l[2])
                else:
                    break
    return numbers