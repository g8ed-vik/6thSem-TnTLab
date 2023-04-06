#take two studentlist in separate dictionary
#merge 2 dictionary
#print student names in alphabetical order
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

student_dict1={}
for i in studentlist1:
    if i in student_dict1:
        student_dict1[i] += 1
    else:
        student_dict1[i] = 1

student_dict2={}
for i in studentlist2:
    if i in student_dict2:
        student_dict2[i] += 1
    else:
        student_dict2[i] = 1


student_dict2.update(student_dict1)

print(student_dict2)

for i in  student_dict2:
    print(i)
        