def rotatestring(s,goal):
    if len(s)!=len(goal):
        return False
    return True if s in goal+goal else False

s=input()
goal=input()
print(rotatestring(s,goal))