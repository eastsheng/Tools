#write data from cnb to graphene
def write_data(filename1,filename2):
	with open(filename1,'r') as former:
		for index,line in enumerate(former,1):
			if "Atoms # full" in line:
				# print(index)
				line_cut = index #头信息与位置信息分割线
			elif "Masses" in line:
				# print(index)
				mass_line = index
	#write 头信息			
	with open(filename1,'r') as former, open(filename2,'w') as latter:		
		for index,line in enumerate(former,1):
			line_ss = line.strip().split()
			if index<=line_cut:
				# print(line)
				if "atom types" in line:
					latter.write(' 1 atom types\n')
				elif index>mass_line and index<line_cut and line_ss!=[] and " 1 " in line:
					# print(index)
					latter.write(line)
				elif " 2 " in line or " 3 " in line:
					pass
					# print(line)
				else:
					latter.write(line)
		latter.write('\n')
	#write 位置信息
	with open(filename1,'r') as former, open(filename2,'a') as latter:		
		for index,line in enumerate(former,1):
			line_ss = line.strip().split()
			if index>line_cut and line_ss!=[]:
				latter.write(line_ss[0]+' '+line_ss[1]+' '+str(1)+' '+line_ss[3]+' '+line_ss[4]+' '+line_ss[5]+\
							 ' '+line_ss[6]+' '+line_ss[7]+' '+line_ss[8]+\
							 ' '+line_ss[9]+'\n')



	
	return print('write_dataforTransmission() done!')


write_data('cnb.data','graphene.data')

print('*******************')
print('****   Done!   ****')
print('****   Done!   ****')
print('*******************')