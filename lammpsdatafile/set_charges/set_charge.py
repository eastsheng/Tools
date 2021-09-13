# set charges from ligpargen for the heavy oil molecules

def set_charge(key):
    charge_list = []
    with open(key,'r') as sc:
        for index, line in enumerate(sc,1):
            # print(line)
            if "charge" in line:
                # print(line)
                list_line = "".join(line).split()
                # print(list_line[2])
                charge_list.append(list_line[2])
        # print(charge_list)

    return charge_list

if __name__ == '__main__':
    key1 = "saturate_optimized_ligpargen.key"
    key2 = "aromatic_optimized_ligpargen.key"
    key3 = "resin_optimized_ligpargen.key"
    key4 = "asphaltene_optimized_ligpargen.key"
    charge_file = "system.in.charge"
    charge_list_1 = set_charge(key1)
    charge_list_2 = set_charge(key2)
    charge_list_3 = set_charge(key3)
    charge_list_4 = set_charge(key4)
    len1 = len(charge_list_1)
    len2 = len(charge_list_2)
    len3 = len(charge_list_3)
    len4 = len(charge_list_4)
    # print(len1,len2,len3,len4)
    with open(charge_file,'w') as cf:
        for i in range(len1):
            cf.write("set type "+str(i+1)+" charge "+charge_list_1[i-1]+'\n')

        for i in range(len1,len1+len2):
            cf.write("set type "+str(i+1)+" charge "+charge_list_2[i-len1-1]+'\n')
        for i in range(len1+len2,len1+len2+len3):
            cf.write("set type "+str(i+1)+" charge "+charge_list_3[i-len1-len2-1]+'\n')
        for i in range(len1+len2+len3,len1+len2+len3+len4):
            cf.write("set type "+str(i+1)+" charge "+charge_list_4[i-len1-len2-len3-1]+'\n')
