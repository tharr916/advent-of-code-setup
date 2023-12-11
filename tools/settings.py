"""Important settings for the app"""
from datetime import datetime
from configparser import ConfigParser
import logging

CONFIG: ConfigParser | None = None


def get_config_value(section: str, key: str) -> str:
    """Returns the config value"""
    if not CONFIG:
        run_config()
    assert CONFIG is not None
    return CONFIG[section][key]


def run_config():
    """Sets up the config"""
    # pylint: disable-next=global-statement
    global CONFIG
    if CONFIG is not None:
        return
    CONFIG = ConfigParser()
    CONFIG.read("./config/config.ini")
    logging.info("Config file loaded")


def get_session_id(file: str) -> str:
    """Returns the session id from the given file"""
    with open(file, "r", encoding="utf8") as f:
        return f.read().strip()


def get_year() -> int:
    """Returns the year"""
    return int(get_config_value("adventofcode", "year"))


def get_username() -> str:
    """Returns the username"""
    return get_config_value("general", "user")


def get_repo_name() -> str:
    """Returns the repository name"""
    return get_config_value("adventofcode", "repo_name")


def get_session_cookie_path() -> str:
    """Returns the session id string"""
    return get_config_value("adventofcode", "session_cookie_file")


SESSION_COOKIE_FILE: str = get_session_cookie_path()
USER_AGENT_PARTS: tuple[str, str] = (get_username(), get_repo_name())
YEAR: int = get_year()
