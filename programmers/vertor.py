
total_arr = []
part_arr = []



for i in range(1,32):
    for j in range(1,32):
        if i==j:
            part_arr.append('R')
        else:
            part_arr.append('rz'+ str(j))
    total_arr.append(part_arr)
    part_arr = []


for i in total_arr:
    print(i)