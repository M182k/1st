# School Administration Programe

import csv

def write_into_csv(info_list):
	with open('student_info.csv','a',newline=' ')as csv_file:
		writer = csv.writer(csv_file)
		
		if csv_file.tell() == 0 :
			writer.writerow(["Name","Age","Contact_Number","E-mail_Id"])
			
			write.writerow(info_list)
			
if__name__ == '__main__':
	condition = True
	student_num = 1
	
	while(condition):
		student_info = input('Enter student information for student n{} in the following format[Name Age Contact_Number E-mail_Id]: ').format (student_num)
		
		student_info_list = student_info.split()
		
		print"\n The Entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nE-mail_Id: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
		
		choice_check = input("Is the Entered information is correct? (yes/no:")
		
		if choice_check =="yes":
			write_info_csv(student_info_list)
			
			condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
			if condition_check == "yes":
				condition = True
				student_num = student_num + 1
			elif condition_check =="no":
				condition = False
				
		elif chice_check == "no":
			print("\Please re-enter the values!")
