def sum(inp):
    tot=0
    for i in inp:
        tot+=i
    return tot

def reverse_str(torev):
    return torev[::-1]

print("Sum of all items in list is :", sum([8, 5, 6]))