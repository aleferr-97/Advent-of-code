def detectStart(file):

    i = 0
    reader = open(file, 'r')
    line = reader.readline()
    detector = list()
    newDetector = list()
    result = 0

    while len(detector) < 14:
        if line[i] not in detector:
            detector.append(line[i])
        else:
            for index in range(i-len(detector),i):
                if line[index] != line[i]:
                    newDetector.append(line[index])
                else:
                    del newDetector[len(newDetector)-index:len(newDetector)]
            newDetector.append(line[i])
            detector = newDetector.copy()
            newDetector.clear()

        i += 1
        result += 1

    return result

if __name__ == "__main__":
    file = 'input.txt'
    result = detectStart(file)
    print(str(result))
