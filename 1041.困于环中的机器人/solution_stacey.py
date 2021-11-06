def isRobotBounded(instructions):
    dir = [0,0,0,0]
    res = 0
    for i in instructions:
        if i == 'G':
            res = res % 4
            dir[res]+=1
            continue
        elif i == 'L':
            res += 1
        else:
            res -= 1
    if dir[0]-dir[2] ==0 or dir[3] - dir[1]==0: return False
    return True

print(isRobotBounded("GLGLGGLG"))