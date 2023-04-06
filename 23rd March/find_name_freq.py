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


# find frequency of student names from student list

# student_dict1={}
# for i in studentlist1:
#     if i in student_dict1:
#         student_dict1[i] += 1
#     else:
#         student_dict1[i] = 1
# print(student_dict1)

# student_dict2={}
# for i in studentlist2:
#     if i in student_dict2:
#         student_dict2[i] += 1
#     else:
#         student_dict2[i] = 1
# print(student_dict2)

#find frequency of student names on the basis of their first letter from student list

studentlist1.extend(studentlist2)
student_dict3={}
for i in studentlist1:
    if i[0] in student_dict3:
        student_dict3[i[0]] += 1
    else:
        student_dict3[i[0]] = 1 
print(student_dict3)
