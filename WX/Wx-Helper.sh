#!/bin/sh


FILE=$HOME/WX/.wx
if test -f "$FILE"; then
    echo
else

chmod +x /$HOME/WX/Resources/code_gen

touch .wx

fi

echo Enter the number of the Weather Station type:
echo 1. LaCrosse-TX
echo 2. Bresser 3-Channel
echo 3. Nexus-TH
echo 4. 
echo 5. 

read num

cd $HOME/WX/

case "$num" in
   "1") python3 Resources/lacrosse.py 
   
   Resources/./code_gen -s 250k -r $HOME/WX/Output/lacrosse.txt -w $HOME/WX/Output/lacrosse.cu8
   
   rtl_433 -r $HOME/WX/Output/lacrosse.cu8 -w $HOME/WX/Output/lacrosse.ook
   
   python3 Resources/subghz_ook_to_sub.py $HOME/WX/Output/lacrosse.ook 433920000
   
   rm $HOME/WX/Output/lacrosse.txt
   
   rm $HOME/WX/Output/lacrosse.cu8
   
   rm $HOME/WX/Output/lacrosse.ook
   
   exit 1
   ;;
   "2") python3 Resources/bresser3ch.py 
   
   Resources/./code_gen -s 250k -r $HOME/WX/Output/bresser3ch.txt -w $HOME/WX/Output/bresser3ch.cu8
   
   rtl_433 -r $HOME/WX/Output/bresser3ch.cu8 -w $HOME/WX/Output/bresser3ch.ook
   
   python3 Resources/subghz_ook_to_sub.py $HOME/WX/Output/bresser3ch.ook 433920000
   
   rm $HOME/WX/Output/bresser3ch.txt
   
   rm $HOME/WX/Output/bresser3ch.cu8
   
   rm $HOME/WX/Output/bresser3ch.ook
   
   exit 1
   ;;
   
   "3") python3 Resources/nexus-th.py 
   
   Resources/./code_gen -s 250k -r $HOME/WX/Output/nexus.txt -w $HOME/WX/Output/nexus.cu8
   
   rtl_433 -r $HOME/WX/Output/nexus.cu8 -w $HOME/WX/Output/nexus.ook
   
   python3 Resources/subghz_ook_to_sub.py $HOME/WX/Output/nexus.ook 433920000
   
   rm $HOME/WX/Output/nexus.txt
   
   rm $HOME/WX/Output/nexus.cu8
   
   rm $HOME/WX/Output/nexus.ook
   
   exit 1
   ;;
   
   "4")
   
   exit 1
   ;;
   
   "5")
   
    exit 1
    ;;
   
esac

