fp = open(r"D:\GIT-DEMO\LocalRepo\data.txt", 'r')
#data=fp.read()
#data=fp.readline(11)
data=fp.readlines()
print(data[0:2])

fp.close()