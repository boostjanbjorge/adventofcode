#part 1
import statistics as st
def crabby_fuel(inputs):
    optimal_position=st.median(inputs)
    return sum(abs(pos-optimal_position) for pos in input)

#part 2
def sgn(x):
    if x>=0:
        return 1
    return 0

def iterate_position(init_pos, inputs):
    pos=init_pos
    p0=pos+1
    while abs(pos-p0)>=0.1:
        p0=pos
        pos=sum(x-0.5*sgn(x-pos) for x in inputs)/len(inputs)
    return round(pos)

def crabby_fuel_expensive(inputs):
    optimal_position = iterate_position(0,inputs)
    return sum(((pos-optimal_position)**2+abs(pos-optimal_position))/2 for pos in inputs)
