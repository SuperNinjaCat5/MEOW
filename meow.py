console = Console()


import os
import sys
if debug_mode == True:
    from rich.console import Console



debug_mode = False

def debug_print(message):
    if debug_mode:
        print(message)

class meow_lang:
    def __init__(self, filename):
        self.functions = {
            "paw": "def",
            "purr": "print"
        }
        self.filename = filename

    def read_code(self):
        with open(self.filename, "r") as f:
            code = f.read()
        return code

    def translate_code(self):
        code = self.read_code()
        for function in self.functions:
            current = self.functions.get(function)
            debug_print(f"line 26: {current}")
            code = code.replace(function, current)
        debug_print(f"line 28: {code}")
        return code

    def execute_code(self):
        executed_code = self.translate_code()
        exec(executed_code)

def meow(filepath):
    meow_language_instance = meow_lang(filepath)
    meow_language_instance.execute_code()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: meow <filename.meow>")
        sys.exit(1)
    else:
        meow(sys.argv[1])