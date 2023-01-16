import time
import os
import sys

home_directory = os.path.expanduser( '~' )

def main():
    
    id = int(input('What is the ID number?\n'))
    id = format(id, '08b')
    
    flag = str('10')
    
    ch = int(input('What is the channel number?\n'))
    if ch == 1:
        ch = str('00')
    elif ch == 2:
        ch = str('01')
    elif ch == 3:
        ch = str('10')
    else:
        sys.exit("Invalid channel, 1-3")
    
    temp = float(input('Enter temp: 3 digits in C eg 19.4: 205.0 is lowest 200.0 is highest (rollover), \n'))
    temp = str(temp).replace('.', '')
    temp = bin(int(temp))
    temp = str(temp).replace('0b','')
    temp = str(temp).zfill(12)
    
    const = str('1111')
    
    humid = int(input('What is the humidity in whole numbers?\n'))
    humid = format(humid, '08b')
    
    f = open(os.path.join( home_directory, 'WX', 'Output', 'nexus.txt'),"w")
    f.write("[~ (40kHz) ]\n[_ (3000us) ]\n[0 (~500us) (1000us) ]\n[1 (~500us) (2000us) ]\n\n\n_ _ _\n")
    f.close()
    
    final = id + flag + ch + temp + const + humid
    
    print('final = %s' % final)
    
    for x in range(100):
        f = open(os.path.join( home_directory, 'WX', 'Output', 'nexus.txt'),"a")
        f.write("%s0_\n" % final)
        f.close()
    
if __name__ == '__main__':
    main()