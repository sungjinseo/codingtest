def solution(genres, plays):
    answer = []
    music_map = {}
    for i in range(len(genres)):
        if genres[i] in music_map.keys():
            music_map[genres[i]].append([plays[i], i])
            music_map[genres[i]][0] += plays[i]
        else:
            music_map[genres[i]] = [plays[i], [plays[i], i]]
    sort_dict = sorted(music_map.items(), key=lambda item:item[1], reverse=True)
    
    for key in music_map.keys():
        music_map[key][1:] = sorted(music_map[key][1:], key=lambda x:(x[0],x[1]), reverse=True)
    
    
    for key in sort_dict:
        if len(music_map[key[0]]) == 2:
            answer.append(music_map[key[0]][1][1])
        else:
            answer.append(music_map[key[0]][1][1])
            answer.append(music_map[key[0]][2][1])     

    return answer

if __name__ == '__main__':
    temp = solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500])
    print(temp)