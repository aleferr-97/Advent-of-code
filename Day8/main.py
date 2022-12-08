def countVisibles(file):

    gridVr, gridOr = defineGrid(file)
    reader = open(file, 'r')
    lines = reader.readlines()
    visibles = 0
    visibles += (len(lines)-2)*2
    maxLength = len(max(lines, key=len)) - 1
    visibles += maxLength*2

    i = 0
    y = 1
    for line in lines:
        if i == 0 or i == len(lines)-1:
            pass
        else:
            for y in range(1, len(line)-2):
                a = i
                b = y
                elem = gridOr[i][y]
                left = gridOr[i][0:y]
                right = gridOr[i][y + 1:len(line)]
                top = gridVr[y][0:i]
                bottom = gridVr[y][i+1:len(lines)]

                if all(x < elem for x in left):
                    visibles += 1
                elif all(x < elem for x in right):
                    visibles += 1
                elif all(x < elem for x in top):
                    visibles += 1
                elif all(x < elem for x in bottom):
                    visibles += 1
        i += 1


    print(visibles)
    reader.close()

def calcScenicScore(file):
    gridVr, gridOr = defineGrid(file)
    reader = open(file, 'r')
    lines = reader.readlines()
    scenicScore = 1
    maxScenicScore = 0
    i = 0
    count = 0
    length = len(max(lines, key=len)) - 1
    left = 0
    right = 0
    top = 0
    bottom = 0


    for line in lines:
        for y in range(0, length):
            elem = gridOr[i][y]

            for index in range(y-1, -1, -1):
                sx = gridOr[i][index]
                if gridOr[i][index] < elem:
                    count += 1
                    left += 1
                elif gridOr[i][index] == elem:
                    count += 1
                    left += 1
                    break
                else:
                    count += 1
                    left += 1
                    break
            if left == 0:
                count = 1
            else:
                left = 0
            scenicScore *= count
            count = 0
            for index in range(y+1, length):
                dx = gridOr[i][index]
                if gridOr[i][index] < elem:
                    count += 1
                    right += 1
                elif gridOr[i][index] == elem:
                    count += 1
                    right += 1
                    break
                else:
                    count += 1
                    right += 1
                    break
            if right == 0:
                count = 1
            else:
                right = 0
            scenicScore *= count
            count = 0
            for index in range(i-1, -1, -1):
                up = gridVr[y][index]
                if gridVr[y][index] < elem:
                    count += 1
                    top += 1
                elif gridVr[y][index] == elem:
                    count += 1
                    top += 1
                    break
                else:
                    count += 1
                    top += 1
                    break
            if top == 0:
                count = 1
            else:
                top = 0
            scenicScore *= count
            count = 0
            for index in range(i+1, length):
                down = gridVr[y][index]
                if gridVr[y][index] < elem:
                    count += 1
                    bottom += 1
                elif gridVr[y][index] == elem:
                    count += 1
                    bottom += 1
                    break
                else:
                    count += 1
                    bottom += 1
                    break
            if bottom == 0:
                count = 1
            else:
                bottom = 0
            scenicScore *= count
            count = 0
            if scenicScore > maxScenicScore:
                maxScenicScore = scenicScore
                count = 0
            scenicScore = 1

        i += 1
    print(maxScenicScore)


def defineGrid(file):
    reader = open(file, 'r')
    lines = reader.readlines()
    gridOr = []
    gridVr = []
    maxLength = len(max(lines[:], key=len)) - 1

    for line in lines:
        singleLine = []
        for j in range(0, maxLength):
            if line[j] != '0':
                singleLine.append(int(line[j]))
            else:
                singleLine.append(0)

        gridOr.append(singleLine)

    reader.close()

    reader = open(file, 'r')
    lines = reader.readlines()

    for i in range(len(lines)):

        gridVr.append([int(sublist[i]) for sublist in lines])

    reader.close()
    return gridVr, gridOr


if __name__ == "__main__":
    file = 'input.txt'
    #countVisibles(file)
    calcScenicScore(file)
