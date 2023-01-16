import os 
import time
import itertools

home_directory = os.path.expanduser( '~' )

def main():
    
    pre= str('0000')
    amb= str('1010')
    le= str('0000')
    
    preamble = pre+amb+le

    id = int(input('What is the ID number?\n'))
    id = format(id, '07b')
    
    parity= str('0')
    parity1= str('1')
    
    temp = float(input('Enter temp: 3 digits in C eg 20.5, 49.9 max temp 50.0 min temp\n'))
    temp = round(temp, 1) + 50
    temp = str(temp).replace('.', '')
    s1 = slice(1)
    s2 = slice(1,2)
    s3 = slice(2,3)
    v1 = temp[s1]
    v2 = temp[s2]
    v3 = temp[s3]
    v1 = bin(int(v1))
    v2 = bin(int(v2))
    v3 = bin(int(v3))
    v1 = str(v1).replace('0b','')
    v2 = str(v2).replace('0b','')
    v3 = str(v3).replace('0b','')
    v1 = str(v1).zfill(4)
    v2 = str(v2).zfill(4)
    v3 = str(v3).zfill(4)
    
    id1 = id + parity
    id2 = id + parity1
    
    f = open(os.path.join( home_directory, 'WX', 'Output', 'lacrosse.txt'),"w")
    f.write("[~ (40kHz) ]\n[_ (7244us) ]\n[0 (~1400us) (1000us) ]\n[1 (~500us) (1000us) ]\n\n\n_ _ _\n")
    f.close()
    
    chk1 = int(pre, 2) + int(amb, 2) + int(le, 2) + int(id1[0:4], 2) + int(id1[4:8], 2) + int(v1, 2) + int(v2, 2) + int(v3, 2) + int(v1, 2) + int(v2, 2)
    chk1 = bin(chk1)
    chk1 = str(chk1[-4:])
    
    chk2 = int(pre, 2) + int(amb, 2) + int(le, 2) + int(id2[0:4], 2) + int(id2[4:8], 2) + int(v1, 2) + int(v2, 2) + int(v3, 2) + int(v1, 2) + int(v2, 2)
    chk2 = bin(chk2)
    chk2 = str(chk2[-4:])
    
    final1 = preamble + id + parity + v1 + v2 + v3 + v1 + v2 + chk1 
    print('%s' % final1)
    
    final2 = preamble + id + parity1 + v1 + v2 + v3 + v1 + v2 + chk2  
    print('%s' % final2)
    
    f = open(os.path.join( home_directory, 'WX', 'Output', 'lacrosse.txt'),"a")
    
    for i in range(100):
        f.write("%s_\n" % final1)
        f.write("%s_\n" % final2)
    
    f.close()
    
    
if __name__ == '__main__':
    main()