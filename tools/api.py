"""API for the AoC website"""
from os.path import exists
import requests
from tools.settings import SESSION_COOKIE_FILE, USER_AGENT_PARTS, YEAR


def get_session_id(filename):
    """Returns the session id from the given file"""
    with open(filename, "r", encoding="utf8") as f:
        return f.read().strip()


def get_user_agent() -> str:
    """Returns the user agent"""
    username, repo_name = USER_AGENT_PARTS
    return f"https://github.com/{username}/{repo_name}, discord:@{username}, reddit:u/{username}"


def get_url(year, day) -> str:
    """Returns the url for the input of the given day"""
    return f"https://adventofcode.com/{year}/day/{day}/input"


SESSION = get_session_id(SESSION_COOKIE_FILE)
HEADERS = {
    "User-Agent": get_user_agent(),
}
COOKIES = {"session": SESSION}


def get_input(day) -> str:
    """Retrieves the input for the given day"""
    path = f"inputs/{day:02d}"

    if not exists(path):
        url = get_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=60)
        if not response.ok:
            raise RuntimeError(
                f"Request failed \
                  \n\tstatus code: {response.status_code} \
                  \n\tmessage: {response.content}"
            )
        with open(path, "w", encoding="utf8") as f:
            f.write(response.text[:-1])

    with open(path, "r", encoding="utf8") as f:
        return f.read()
