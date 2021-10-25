# function to see if a string is 1 edit or 0 edits away
Input = "pale", "ple"

def one_away(a, b):
    x, y, i, j, count = len(a), len(b), 0, 0, 0
    if abs(x - y) > 1:
        return False
    while i < x and j < y: 
        if a[i] != b[j]:
            if count == 1:
                return False
            if x < y:
                j = j + 1
            elif x > y:
                i = i + 1
            else:
                i = i + 1
                j = j + 1
            count = count + 1
        else:
            i = i + 1
            j = j + 1
    if i < x or j < y:
        count = count + 1
    return count == 1
    
    if one_away(a, b):
        print("true")
    else:
        print("false")

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))