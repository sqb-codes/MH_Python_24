# copy paste working using python
import time

file = open("img_1.png", "rb")
data = file.read()
file.close()

# print(len(data))

SIZE = len(data)

BUFFERSIZE = 5000 # 5KB data

startSize = 0
endSize = BUFFERSIZE

for i in range(SIZE):
    file = open("img_copy.png", "ab")
    file.write(data[startSize:endSize])
    file.close()
    time.sleep(3)
    startSize += BUFFERSIZE
    endSize += BUFFERSIZE

