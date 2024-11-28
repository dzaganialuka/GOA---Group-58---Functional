txt = '    Cats   go   meow   '

def space_cull(string):

    word = string.split(" ")
    result = ""
    for elem in word:
        if not elem == '':
            result += str(elem) + ' '
    return result.strip()

print(space_cull(txt))