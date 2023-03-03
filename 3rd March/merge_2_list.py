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


#Merge the 2 student lists

studentlist1.extend(studentlist2)

print(studentlist1)