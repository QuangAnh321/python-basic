# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


# print(GREEN, "this will be in Green")
# print(YELLOW, "this will be in yellow")

def color_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequence to modify the string
     like changing the color, etc

    :param text: The text to print
    :param effects: The effect to apply to the string. It is one of the constants
        defined in the start of this file
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


color_print("this is red", RED)
print("Default")
color_print("this is bold", BOLD)
color_print("This is green and underline", GREEN, UNDERLINE)
