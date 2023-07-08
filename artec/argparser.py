"""
	Parser class is a wrapper for easy access of argparse module
"""
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter, _VersionAction
from .templates import templates
import sys


class list_templates(_VersionAction):
    def __call__(self, parser: ArgumentParser, *args, **kwargs) -> None:
        formatter = parser._get_formatter()
        formatter.add_text(
            "Available templates\n\n"
            + "\n".join([f"> {key.title()}\t" for key, value in templates.items()])
        )
        parser._print_message(formatter.format_help(), sys.stdout)
        parser.exit()


class Parser(ArgumentParser):
    def __init__(self, appVersion):
        self.appVersion = appVersion
        prog = "Artec"
        usage = "artec [OPTIONS] -o [DEST] "
        description = "Artec is a simple python 3 script to create a project template in a given directory."
        epilog = "Examples:\n\tartec -h\n\tartec -o dest\
            \n\tartec -o dest -t python \n\tartec -o dest -s structure.json \n\tartec -o dest -s structure.json -v"
        super().__init__(
            prog, usage, description, epilog, formatter_class=RawTextHelpFormatter
        )

    def setup(self):
        self.add_argument(
            "-o",
            "--output-directory",
            dest="target",
            help="Target output path where the structure will be created",
            type=str,
            required=True,
        )

        self.add_argument(
            "-s",
            "--source-file",
            dest="source",
            help="Source JSON file containing structure to be created",
            type=str,
            required=False,
        )
        self.add_argument(
            "-t",
            "--template",
            dest="template",
            help="Uses ready-made templates.",
            required=False,
        )

        self.add_argument(
            "-ls",
            "--list-template",
            help="lists all ready-made templates.",
            action=list_templates,
        )


        self.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            help="Runs Artec in verbose mode.",
            action="store_true",
            required=False,
        )

        self.add_argument(
            "-V",
            "--version",
            help="Display current version of Artec",
            action="version",
            version=f"{self.prog} {self.appVersion}",
        )


def main_args(appVersion) -> Namespace:
    parser = Parser(appVersion)
    parser.setup()
    return parser.parse_args()


if __name__ == "__main__":
    pass
