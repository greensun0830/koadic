DESCRIPTION = "PBR Friday"

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):

    print(open("data/papst.txt", "rb").read().decode("unicode_escape")[0:1583])
