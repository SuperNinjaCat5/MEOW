
debug_mode = True

def debug_print(message):
    if debug_mode:
        print(message)

import os
import sys
import tokenize
import io

if debug_mode == True: # This is just for dev
    from rich.console import Console
    console = Console()
    def debug_print(message):
        if debug_mode:
            console.log(message)

class meow_lang:
    def __init__(self, filename):
        self.functions = {
            "paw": "def",
            "meow": "print",
            "lick": "input",
            "cat": "class",
            "dog": "tuple",
            "pet": "return",
            "i_will_toss_you_into_the_dark_void_of_doom_and_let_you_rot_as_the_monsters_suck_your_soul": "pass",
            "walk": "continue",
            "rest": "sleep",
            "cease_thou_silly_tendencies_or_anon_shalt_i_unleash_the_wrath_of_the_cat_gods_upon_thee": "break",
        }
        self.filename = filename

    def read_code(self):
        with open(self.filename, "r") as f:
            code = f.read()
        return code



    def translate_code(self):
        code = self.read_code()
        functions = self.functions

        result = []
        tokens = tokenize.generate_tokens(io.StringIO(code).readline)
        for toknum, tokval, _, _, _ in tokens:
            if toknum == tokenize.NAME and tokval in functions:
                tokval = functions[tokval]
            result.append((toknum, tokval))
        return tokenize.untokenize(result)

    def execute_code(self):
        try:
            executed_code = self.translate_code()
            exec(executed_code, globals())
            debug_print("Code executed successfully.")
        except Exception as e:
            print(f"Error executing code: {e}")

def meow(filepath):
    meow_language_instance = meow_lang(filepath)
    meow_language_instance.execute_code()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: meow <filename.meow>")
        sys.exit(1)
    else:
        meow(sys.argv[1])