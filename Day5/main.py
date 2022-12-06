def defineTop(file):
    reader = open(file, 'r')
    lines = reader.readlines()
    i = 0
    matrix = {}
    newMatrix = {}
    finalString = ""
    for line in lines:
        if i < 8:
            matrix[i] = parseMatrix(line,i)
            i += 1
        elif i == 8:
            newMatrix = formatCrates(matrix)
            i += 1
            continue
        elif i == 9:
            i += 1
            continue
        else:
            instruction = line.split()
            #newMatrix = moveCrates(newMatrix,int(instruction[1]),int(instruction[3])-1,int(instruction[5])-1) part1
            newMatrix = moveMoreCrates(newMatrix,int(instruction[1]),int(instruction[3])-1,int(instruction[5])-1) #part 2
    for index in range(len(newMatrix)):
        out = newMatrix[index]
        finalString += out[0]
    return finalString


def parseMatrix(line,i):
    tempList = list()
    count = 0
    j = 0
    crates = line.replace(" ", "-")
    while j < len(crates):
        h = j
        while crates[h] == '-':
            count += 1
            h += 1
            j = h
            if (count % 4) == 0:
                tempList.insert(len(tempList), 0)
        count = 0
        if crates[j] != ']' and crates[j] != '[':
            tempList.append(crates[j])
        j += 1
    return tempList


def formatCrates(matrix):
    newMatrix = {}
    for j in range(len(matrix)+1):
        i = 0
        list1 = list()
        while i <len(matrix):
            listTemp = matrix[i]
            if listTemp[j] != 0:
                list1.append(listTemp[j])
            i += 1
        newMatrix[j] = list1
    return newMatrix


def moveCrates(matrix,many,start,end):
    list1 = matrix[start]
    list2 = matrix[end]
    for i in range(0,many):
        elem = list1[0]
        list1.remove(elem)
        list2.insert(0,elem)
    matrix[start] = list1
    matrix[end] = list2
    return matrix


def moveMoreCrates(matrix,many,start,end):
    list1 = matrix[start]
    list2 = matrix[end]
    movedCrates = list1[0:many]
    list2[0:0] = movedCrates
    del list1[0:many]
    matrix[start] = list1
    matrix[end] = list2
    return matrix

if __name__ == "__main__":
    file = 'input.txt'
    print("Cima delle crates: "+ str(defineTop(file)))
