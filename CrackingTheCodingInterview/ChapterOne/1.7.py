import numpy as numpy

size = 13
zeroSize = size -1
listSize = [x for x in range(1, (size*size)+1)]
sizeChunks = [listSize[i:i + size] for i in range(0, len(listSize), size)]

print(np.matrix(sizeChunks))

temp = 0
for layer in range(0, (size+1)//2):
    for offset in range(0, size - (2*layer) -1):
        temp = sizeChunks[layer][layer+offset]
        sizeChunks[layer][layer+offset] = sizeChunks[layer][layer+offset]
        sizeChunks[zeroSize-layer-offset][layer] = sizeChunks[zeroSize-layer-offset][layer]
        sizeChunks[zeroSize-layer][zeroSize-layer-offset] = sizeChunks[layer+offset][zeroSize-layer]
        sizeChunks[layer+offset][zeroSize-layer] = temp
print(np.matrix(sizeChunks))
