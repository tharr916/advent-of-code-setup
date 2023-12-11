"""Creates a cool `README.md` file with a list of the solutions in the source
   directory, with working links. Note that this original readme will be overwritten.
"""
import os

BASE_LINK = "https://github.com/<USERNAME>/<REPOSITORY_NAME>/blob/main/src/"


def parse(e):
    """Parses the given file name"""
    name = e.replace(".py", "")
    # name = " ".join(name.split("_")[1:])
    return f"[{name}]({BASE_LINK}{e})"


solutions = filter(lambda x: ".py" in x and "init" not in x, os.listdir("./"))

readme_content:str = "# Advent of code\nProblems list:\n"
tmp = [f"{i+1}. {parse(e)}" for i, e in enumerate(sorted(solutions))]
readme_content += "\n".join(tmp)

with open("README.md", "w", encoding="utf8") as f:
    f.write(
        readme_content
        + "\n\nCreated via: [advent-of-code-setup](https://github.com/tomfran/advent-of-code-setup)"
    )
