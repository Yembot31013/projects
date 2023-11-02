import time
import sys
import colorama

def success_print(value):
  print(colorama.Fore.GREEN + value)
  print(colorama.Fore.RESET)
def danger_print(value):
  print(colorama.Fore.RED + value)
  print(colorama.Fore.RESET)
def primary_print(value):
  print(colorama.Fore.BLUE + value)
  print(colorama.Fore.RESET)
def progess_print(value):
  print(colorama.Fore.YELLOW + value)
  print(colorama.Fore.RESET)

def pletter(value, times=1, ends='\n', seps=''):
    for i in value:
        sys.stdout.write(i+seps)
        sys.stdout.flush()
        time.sleep(times)
    sys.stdout.write(ends)


def pword(value, times=1, ends='\n', seps=' '):
    for i in value.split(' '):
        sys.stdout.write(i+seps)
        sys.stdout.flush()
        time.sleep(times)
    sys.stdout.write(ends)


def inputt(meth=pword):
    values = sys.stdin.readline()
    meth(values)

# 1 == 1 seconds


def dput(value, times=1):
    for i in value:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(times)


# 0.01 == 1 seconds


def writelines(value, times=0.01):
    for i in value:
        sys.stdout.write(i)
        time.sleep(times)

def pword_colorful(value, times=0.02, ends='\n', seps=' '):
    colors = [colorama.Fore.GREEN, colorama.Fore.RED, colorama.Fore.BLUE, colorama.Fore.YELLOW]

    for char in value:
        sys.stdout.write(colors.pop(0) + char)
        sys.stdout.flush()
        colors.append(colors[0])  # Rotate the color list
        time.sleep(times)

    sys.stdout.write(colorama.Fore.RESET + ends)

# pword(message, times=0.02, ends='\n', seps=' ')
colorama.init()  # Initialize colorama

pword_colorful(message, times=0.02, ends='\n', seps=' ')

# writelines("""
# i ama a good boy

# i love food
# """)
# def cprint(value, times=1, color='yellow'):
#     for i in value:
#         termcolor.colored(sys.stderr.write(i), color)
#         sys.stderr.flush()
#         time.sleep(times)



# if __name__ == '__main__':
#     inputs = input('enter your vaue: ')
#     times = input('enter the time per seconds: ')
#     if times != '':
#         times = int(times)
#     if times == '':
#         letter(inputs)
#     else:
#         letter(inputs, times)


# word('yemi i am great')
