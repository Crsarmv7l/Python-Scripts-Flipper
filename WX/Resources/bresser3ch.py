import os 
import time

home_directory = os.path.expanduser( '~' )

def main():

    id = int(input('What is the ID number?\n'))
    id = format(id, '08b')
    
    print('house= %s' % id)
    
    flag = str('00')
    
    print('flag= %s' % flag)
    
    ch = int(input('What is the channel number?\n'))
    ch = format(ch, '02b')
    
    print('ch= %s' % ch)
    
    temp = float(input('Enter temp: 3 digits eg 74.4 Max is 140\n'))
    temp = round(temp, 1) + 90
    temp = round(temp *10)
    print('Temp = %s' % temp)
    temp = str(temp).replace('.', '')
    print('Temp = %s' % temp)
    temp = bin(int(temp))
    
    temp = str(temp).replace('0b','')
    temp = str(temp).zfill(12)
    
    print('Temp = %s' % temp)
    
    humid = int(input('What is the humidity in whole numbers?\n'))
    humid = format(humid, '08b')
    print('humid= %s' % humid)
    
    flag = flag + ch
    
    prechk= id + flag + temp + humid
    byte1 = prechk[0:8]
    byte2 = prechk[8:16]
    byte3 = prechk[16:24]
    byte4 = prechk[24:32]
    
    print('check= %s' % prechk)
    print('byte1= %s' % byte1)
    print('byte2= %s' % byte2)
    print('byte3= %s' % byte3)
    print('byte4= %s' % byte4)
    
    sum= (int(byte1, 2) + int(byte2, 2) + int(byte3, 2) + int(byte4, 2))& 0xFF
    sum= bin(sum)
    sum= str(sum).replace('0b','')
    print('sum = %s' % sum)
    
    f = open(os.path.join( home_directory, 'WX', 'Output', 'bresser3ch.txt'),"w")
    f.write("[~ (40kHz) ]\n[_ (1000us) ]\n[0 (~250us) (500us) ]\n[1 (~500us) (250us) ]\n[O (~750us) (750us) ]\n\n_ _ _\n")
    f.close()
    
    final = prechk + sum
    print('final = %s' % final)
    f = open(os.path.join( home_directory, 'WX', 'Output', 'bresser3ch.txt'),"a")
    f.write("\nOOOO%sOOOO" % final)
    for i in range(100):
        f.write("\n%sOOOO" % final)
        
    f.close()
    
if __name__ == '__main__':
    main()