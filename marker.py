"""marks your weeks locally and gives you a sense of what's going on.

IMPORTANT:
You need to move this file into your me directory for it to work. 
"""
import math
import os
import json
import string
from typing import List


def bin_vals(vals: List[int], value: int) -> int:
    vals.sort(reverse=True)
    for v in vals:
        if value > v:
            return v


def to_ints(s: str) -> List[int]:
    letters = string.ascii_letters + " '-"
    return [letters.index(x) for x in s]


def from_ints(indeces: List[int]) -> str:
    letters = string.ascii_letters + " '-"
    return "".join([letters[x] for x in indeces])


def print_message(marks, targets, ave, grades, k):
    print(
        f"""
So far, your overall grade for this course is something like {round(ave)}/{sum([x[1] for x in targets])}, or {math.floor(ave/sum([x[1] for x in targets])*100)}%.
Which gives you the illustrious title of: 
    {from_ints(grades[k])}  👈 this is the title you need to put into the quiz 🐍
Broken down by week, that's:
"""
    )
    [print(f"week {m[0]}: {m[1]}/{t[1]}") for t, m in zip(targets, marks)]
    print(
        """
Bear in mind that this is only your progress 𝘀𝗼 𝗳𝗮𝗿, and that 
this number will feel really low if you haven't done many of 
the sets of exercises yet.
Also, the number isn't final until it's run On Ben's computer,  
so if your number and his number disagree, get in touch!"""
    )


def calculate_weekly_percentages(marks, targets):
    pc = []
    for t, m in zip([x[1] for x in targets], [x[1] for x in marks]):
        if m != 0:
            v = m / t
        else:
            v = 0
        pc.append(v)
    return pc


def get_marks(file_name="trace.json"):
    with open(file_name, "r", encoding="utf-8") as f:
        results = json.load(f)

    marks = [(i + 1, x["mark"]) for i, x in enumerate(results) if type(x) is dict]
    targets = [(1, 12), (2, 34), (3, 34), (4, 7)]  # , (5, 15), (8, 29)]
    return marks, targets


def do_tests(set_numbers: List[int]) -> None:
    for set_name in [f"set{i}" for i in set_numbers]:
        command = f"python ..\\course\\{set_name}\\tests.py"
        os.system(command)


def main():
    do_tests([1, 2, 3, 4])  # , 5, 8]]:

    marks, targets = get_marks()

    pc = calculate_weekly_percentages(marks, targets)

    ave = (sum(pc) / len(pc)) * 100
    grades = {
        0: [28, 7, 8, 11, 3, 17, 4, 13, 53, 18, 52, 15, 24, 19, 7, 14, 13],
        20: [43, 14, 20, 6, 7, 54, 18, 2, 0, 11, 4, 3, 52, 15, 24, 19, 7, 14, 13],
        40: [27, 11, 14, 14, 3, 52, 15, 24, 19, 7, 14, 13],
        60: [43, 14, 24, 0, 11, 52, 15, 24, 19, 7, 14, 13],
        80: [29, 8, 0, 12, 14, 13, 3, 52, 15, 24, 19, 7, 14, 13],
    }

    k = bin_vals(list(grades.keys()), ave)
    print_message(marks, targets, ave, grades, k)


main()
