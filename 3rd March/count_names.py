#count how many times Priyanshu and Himanshu are in the file

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

#count Priyanshu and Himanshu in studentlist1

count_priyanshu=0
count_himanshu=0

for i in studentlist1:
    if i=="PRIYANSHU":
        count_priyanshu+=1
    elif i=="HIMANSHU":
        count_himanshu+=1

print("Priyanshu is present",count_priyanshu,"times")
print("Himanshu is present",count_himanshu,"times")