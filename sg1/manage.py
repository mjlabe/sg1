import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


try:
    from sg1.commands import *
except ImportError:
    raise ImportError(
        "Could not import SG1, are you sure it is installed?"
    )


def main():
    parse_command(sys.argv)
