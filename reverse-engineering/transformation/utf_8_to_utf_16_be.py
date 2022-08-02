#!/usr/bin/env python3
import sys
import argparse

class Main:

    def __init__(self, params):
        # collect the arguments
        self.params = None

        self.set_params(params)

    def get_params(self):
        """
        This will get the parameters.
        """
        return self.params

    def set_params(self, params):
        """
        This will set the params.
        """
        self.params = params

    def parse_params(self):
        """
        This method will parse the parameters.
        """
        parser = argparse.ArgumentParser(
                description="This script will get the utf-8 file and decode it to utf-16-be.")
        parser.add_argument(
                "-f", "--file", help="The file name of the UTF-8 file.", required=True)
        self.set_params(parser.parse_args(self.get_params()))

    def run(self):
        """
        This method will decode the UTF-8 file to UTF-16-BE.
        """
        with open(self.get_params().file, "rb") as source_file:
            contents = source_file.read()
        contents = contents.decode("utf-8").encode("utf-16-be")
        contents = contents.decode("utf-8")
        contents = str(contents)
        # contents = contents[2:-1]
        return contents


if __name__ == "__main__":
    utf_8_2_utf_16 = Main(sys.argv[1:])
    utf_8_2_utf_16.parse_params()
    print(utf_8_2_utf_16.run())

