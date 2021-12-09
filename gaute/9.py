#part 1
with open("input.txt") as f:
    raw_strings=[]
    new_line=f.readline()
    while new_line:
        new_line="".join(new_line.split("\n"))
        raw_strings.append(new_line)
        new_line=f.readline()
import numpy as np
heightmap=np.ones((len(raw_strings)+2,len(raw_strings[0])+2), dtype=np.int32)*10
for i, raw_string in enumerate(raw_strings):
    for j, char in enumerate(raw_string):
        heightmap[i+1,j+1]=int(char)

low_points=find_low_points(heightmap)

#answer part 1
sum(low_point + 1 for _,low_point in low_points)

#part 2
def flatten(list_of_list):
    return [x for l in list_of_list for x in l]

def find_increasing_paths(heightmap, i,j):
    return [(i,j)] + flatten([find_increasing_paths(heightmap,i+x,j+y) for x,y in directions if heightmap[i+x,j+y]<9 and heightmap[i+x,j+y]> heightmap[i,j]])

def product(*args):
    res=1
    for number in args:
        res*=number
    return res

def multiply_basin_sizes(heightmap, low_points):
    return product(*sorted([len(set(find_increasing_paths(heightmap, i, j))) for (i,j),_ in low_points],reverse=True)[:3])

#answer part 2
multiply_basin_sizes(heightmap,low_points)
