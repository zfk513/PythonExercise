'''def dirReduc(arr):
    direction_value = {"NORTH": 1, "SOUTH": -1, "EAST": 2, "WEST": -2}
    a = 'start'
    while a == 'start' or a == 'change':
        a="unchange"
        need_to_remove=[]
        for i in range(len(arr)-1):
            if direction_value[arr[i]] + direction_value[arr[i + 1]] == 0:
               need_to_remove.append(arr[i])
               need_to_remove.append(arr[i+1])
               a = 'change'
        if a=="change":
             for x in need_to_remove:
                 arr.remove(x) #总有list.remove(x) x not in the list 的错误，查不出来，但是其他的例子也还不错，当然，我觉得算法是可以改进         
    else :
      return arr

def dirReduc(arr):
    print(arr)
    dir=(" ".join(arr)).replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'').split()
    return dirReduc(dir) if len(dir) < len(arr) else dir
'''

#print(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']))
for x in range(5):
    if x==0:
        x=x+1
    print(x) 

