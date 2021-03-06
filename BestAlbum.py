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
