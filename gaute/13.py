coordinates=[]
fold_instructions=[]
with open("untitled.txt") as f:
    raw_strings=[]
    new_line=f.readline()
    while new_line:
        new_line=new_line.replace("\n","")
        if len(coord:=new_line.split(","))>1:
            coordinates.append((int(coord[0]), int(coord[1])))
        if len(fold_instr:=new_line.split("fold along x="))>1:
            fold_instructions.append(("x",int(fold_instr[1])))
        if len(fold_instr:=new_line.split("fold along y="))>1:
            fold_instructions.append(("y",int(fold_instr[1])))
        new_line=f.readline()

def fold(along, point, coordinates, bounding_box):
    new_coordinates=set()
    if along=="x":
        (x_min, x_max),y =bounding_box
        new_bounding_box=((min(2*point-x_max,x_min), point), y)
        for x,y in coordinates:
            if x<=point:
                new_coordinates.add((x,y))
            else:
                new_coordinates.add((2*point-x,y))
    else:
        x,(y_min,y_max) =bounding_box
        new_bounding_box=(x, (min(2*point-y_max,y_min), point))
        for x,y in coordinates:
            if y<=point:
                new_coordinates.add((x,y))
            else:
                new_coordinates.add((x,2*point-y))
    return new_coordinates, new_bounding_box

#part 1
for direction, point in fold_instructions[:1]:
    coordinates, bounding_box = fold(direction,point, coordinates, bounding_box)

len(coordinates)

#part 2
for direction, point in fold_instructions[1:]:
    coordinates, bounding_box = fold(direction,point, coordinates, bounding_box)

(x_min, x_max), (y_min, y_max) = bounding_box

for _y in range(y_min,y_max+1):
    print("".join("#" if (_x,_y) in coordinates else "." for _x in range(x_min, x_max+1)))

