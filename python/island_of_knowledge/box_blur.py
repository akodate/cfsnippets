def boxBlur(image):
    rangeX, rangeY = range(1, len(image[0])-1), range(1, len(image)-1)
    rangeCoords = (-1, 0, 1)
    pos = [[(x, y) for x in rangeX] for y in rangeY]
    coords = [(i, j) for i in rangeCoords for j in rangeCoords]
    return [[int(sum([image[j[1]+k[0]][j[0]+k[1]] for k in coords])) // 9 for j in i] for i in pos]