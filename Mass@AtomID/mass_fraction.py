# Calculating the mass fraction of C H O N S system 
# by chends, 2021/9/8

# mass
C_mass, H_mass, O_mass, N_mass, S_mass=(
12.011, 1.008, 15.999, 14.007, 32.06)
per = 100
# saturate   aromatic    resin              asphaltene
# C27 H56    C22 H 12    C27 H22 O3 S       C33 H22 N2 O6 S2
# 41.45%     22.56%      30.78              5.21

"""unit mass of molecules"""
Sat_mass = C_mass*27+H_mass*56
aro_mass = C_mass*22+H_mass*12
res_mass = C_mass*27+H_mass*22+O_mass*3+S_mass
asp_mass = C_mass*33+H_mass*22+N_mass*2+O_mass*6+S_mass*2


def num2w(Sat_num, aro_num, res_num, asp_num):
	"from the number of molecules to mass fraction"
	Sat_totmass = Sat_mass*Sat_num
	aro_totmass = aro_mass*aro_num
	res_totmass = res_mass*res_num
	asp_totmass = asp_mass*asp_num
	tot_mass = Sat_totmass+aro_totmass+res_totmass+asp_totmass
	Sat_w = round((Sat_totmass/tot_mass)*per,2)
	aro_w = round((aro_totmass/tot_mass)*per,2)
	res_w = round((res_totmass/tot_mass)*per,2)
	asp_w = round((asp_totmass/tot_mass)*per,2)
	# w = Sat_w+aro_w+res_w+asp_w
	print(Sat_w,aro_w,res_w,asp_w)
	# print(w)
	return 

def w2num(Sat_w,aro_w,res_w,asp_w):
	"from the mass fraction of molecules to number"
	# 暂时没有好的想法。

	return


# -------------MAIN PROGRAM-------------#
# input the number of molecules
num2w(13,10,9,1)
# num2w(62,46,43,5)
# input the mass fractio of molecules
# w2num(41.45,22.56,30.78,5.21)



