"""File generator for new daily solutions."""
import os

days_dir = os.getcwd()

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir(days_dir))
l = list(l)
print(l)
n = 1
if len(l) > 0:
    last = sorted(l)[-1]
    last = last.split("_")[1].split(".")[0]
    n = int(last) + 1

DEFAULT_FILE = "\n".join(
    [
        f'"""Advent of Code 2023, Day {n}"""',
        "from tools.api import get_input",
        f"\ninput_str = get_input({n})",
        "print(input_str)",
        "\n# WRITE YOUR SOLUTION HERE\n",
    ]
)

day_file = f"day_{n:02d}.py"
with open(os.path.join(days_dir, f"day_{n:02d}.py"), "w", encoding="utf8") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {day_file}")
