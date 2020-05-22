#utf-8
#modify frc 0 >> 0.000000
import io
def frc(frcfile1,frcfile2):
	with io.open(frcfile1,'r') as frc1,io.open(frcfile2,'w') as frc2:
		for index, line in enumerate(frc1,1):
			line_ss = line.strip().split()
			line_length = len(line_ss)
			# print(line_length)
			if line_length in [2,1,6]:
				# print(line)
				frc2.write(line)

			elif line_length == 4:
				if line_ss[1] == '0':
					frc2.write(line_ss[0]+' 0.000000 0.000000 0.000000\n')
				else:
					frc2.write(line)


frc('up.frc','up1.frc')
