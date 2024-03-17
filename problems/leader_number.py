input_list=list(map(int,input().strip('[]').split(',')))#[16, 17, 4, 3, 2]

print(input_list)

for i in range(len(input_list)):

    if input_list[i] > sum([j for j in input_list[i+1:]]):
        print(input_list[i])
        break
