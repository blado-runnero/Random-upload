import os
x = os.listdir("C:/Users/bladeRUNNER/Desktop/data/data/")

ff = open("C:/Users/bladeRUNNER/Desktop/train.txt","w")

for i in x:
	dir = "C:/Users/bladeRUNNER/Desktop/data/data/"
	dirr = dir + i
	f = open(dirr, "r")
	to_write = ""+i
	while True:
		

		line = f.readline()
		floats = [float(x) for x in line.split()]
		if(len(floats)>0) :
			a =floats[1]
			b =floats[2]
			c =floats[3]
			d =floats[4]
			xmin = int((a-(c/2.0))*416)
			xmax = int((a+(c/2.0))*416)
			ymin = int((b-(d/2.0))*416)
			ymax = int((b+(d/2.0))*416)
			to_write = to_write + " "+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+",0"
			#print(to_write)
		if not line:
			print(to_write)
			ff.write(to_write+"\n")
			break
	f.close()
ff.close()