import html
import os
import re

import bs4
import requests

CURRENT_YEAR = 2021


def auth_cookie():
    with open(".aoc_session", mode="r") as f:
        session = f.readline().rstrip("\n")
        return dict(session=session)


def problem_url(day, year=CURRENT_YEAR):
    return f"https://adventofcode.com/{year}/day/{day}"


def example(day, year=CURRENT_YEAR):
    fname = f"example.{day}"
    if not os.path.exists(fname):
        with open(fname, mode="w+") as f:
            problem_html = requests.get(problem_url(day, year)).text
            candidates = re.findall(
                r"<pre><code>(.*?)</code></pre>", problem_html, flags=re.DOTALL
            )
            candidates = [
                html.unescape(text).replace("|\n", "| ")
                for text in candidates
                if not bs4.BeautifulSoup(text, "html.parser").find()
            ]

            if (num_cand := len(candidates)) != 1:
                print(f"Warning: Could not find a unique example (found {num_cand})")

            f.write(candidates[0])

    with open(fname, mode="r") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def input(day, year=CURRENT_YEAR):
    fname = f"input.{day}"
    if not os.path.exists(fname):
        with open(fname, mode="w+") as f:
            problem_input = requests.get(
                f"{problem_url(day, year)}/input",
                cookies=auth_cookie(),
            ).text
            f.write(problem_input)

    with open(fname, mode="r") as f:
        return [line.rstrip("\n") for line in f.readlines()]
