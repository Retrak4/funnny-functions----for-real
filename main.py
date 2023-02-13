#problen uno
def Howdy(name):
    print("Howdy", name)

Howdy('Wray')

#problen dous
def number(multiply):
    return multiply*10

print(number(9))

#problem tree

def charinstring(char, string):

    number_of_times = 0

    for letter in string:
        if letter == char:
            number_of_times += 1

    return number_of_times
print(charinstring("a", "wraya"))

#problem fourt

def pos(string1, string2):

    times = 0
    for ind, lett in enumerate(string2):
        if lett == string1[ind]:
            times += 1

    return times
print(pos("krat", "wray"))