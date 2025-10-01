fp=open('data.txt','r')
data=fp.read()

wf=open('data1.txt','w')
d=wf.write(data)
print("New file is created.")
fp.close()
wf.close()