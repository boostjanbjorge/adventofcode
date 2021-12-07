import dataclasses
import collections


@dataclasses.dataclass
class Fish:
    timer: int

    def spwn(self):
        if self.timer == 0:
            self.timer = 6
            return True
        self.timer = self.timer - 1
        return False


def school():
    with open("inputs/6.txt") as f:
        yield from map(int, f.readline().split(","))


def slow_incubate(days: int):
    _school = list(map(Fish, school()))
    for _ in range(days):
        new = [Fish(8) for fish in _school if fish.spwn()]
        _school.extend(new)
    return len(_school)


def incubate(days: int):

    yesterday = collections.Counter(school())

    for _ in range(days):
        today = collections.Counter()
        for timer, cnt in yesterday.items():
            if timer == 0:
                today[8] += cnt
                today[6] += cnt
            else:
                today[timer - 1] += cnt
        yesterday = today

    return sum(today.values())


# 307200 (to low)
print("a:", slow_incubate(80))
print("a:", incubate(80))
print("b:", incubate(256))
