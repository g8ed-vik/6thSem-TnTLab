def readlide_returnList(filename):
	name_list=[]
	file=open(filename,'r')
	for i in file.readlines():
		name_list.append(i.rstrip("\n"))
	return(name_list)

filename1='student1.csv'
filename2='student2.csv'

studentlist1=readlide_returnList(filename1)
studentlist2=readlide_returnList(filename2)


#print(studentlist1)
#print(studentlist2)

#print student names one by one
for i in studentlist1:
	print(i)
for i in studentlist2:
	print(i)
