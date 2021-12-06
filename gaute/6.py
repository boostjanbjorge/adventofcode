from functools import lru_cache

@lru_cache(maxsize=None)
def count_fish(days_lived):
    n_children=max(int((days_lived-2)/7),0)
    return sum(count_fish(days_lived-2-(i+1)*7) for i in range(n_children))+1

def solution(init_state, days_passed):
    return sum(count_fish(days_passed+8-incubation) for incubation in init_state)
