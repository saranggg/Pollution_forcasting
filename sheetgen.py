import pandas as pd
import numpy as np
import glob

flist=glob.glob("NitrogenOxide/*.csv")
flist=[s.strip('.csv') for s in flist]
flist.sort(key = lambda x: int(x.rsplit('_',1)[1]))
flist=[s + ".csv" for s in flist]

for nfile in flist:
	df = pd.read_csv(str(nfile),error_bad_lines=False,header=None,skiprows=5)
	data=df.values
	# print(data)
	arr=np.delete(data, np.s_[:1], axis=1)
	llist=[]
	for x in range(len(arr)):
		# print(arr[x])
		# print(x)
		temp=arr[x].tolist()
		for x1 in range(len(temp)):
			llist.append(temp[(len(temp)-1)-x1])
			ts=temp[(len(temp)-1)-x1]
			import csv
			out = csv.writer(open("NitrogenOxide.csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
			out.writerow([ts])
	ars=np.array(llist)
	Ox3=np.reshape(ars, (len(llist), 1))