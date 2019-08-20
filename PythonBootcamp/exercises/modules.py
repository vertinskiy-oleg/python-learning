from termcolor import colored
from pyfiglet import figlet_format as ff

user_txt = input("Waht message do you want to enter?: ")
user_color = input("What color?: ").lower()
valid_colors = ('red', 'green', 'yellow',
                'blue', 'magenta', 'cyan', 'white')

if user_color not in valid_colors or user_color == "":
    user_color = 'red'

fig_txt = ff(user_txt)
col_txt = colored(fig_txt, color=user_color)

print(fig_txt)
print(col_txt)
