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

#remove duplicate names from studentlist1

studentlist1=set(studentlist1)
studentlist1=list(studentlist1)

studentlist2=set(studentlist2)
studentlist2=list(studentlist2)
print(studentlist1)
print(studentlist2)

        
