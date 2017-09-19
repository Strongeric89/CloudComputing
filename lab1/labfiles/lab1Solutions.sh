#LAB1 - Cloud Computing - Eric Strong
#!/bin/bash
# 1. how many words are in words file
echo "1.number of words in the words file: "
wc -w words

# 2. number of words that start with a
echo "2.number of words that start with a: "
grep ^a words | wc -l

#3. 
echo "3.number of words ending with z: "
grep z$ words | wc -l

#4. create a copy of words in reverse
echo "4.creating copy of words in reverse..."
cat words | sort -r > revWords

#5. how many words contain vowels
echo "5.number of words containing vowels [a,e,i,o,u]: "
cat words | grep -v '[a,e,i,o,u]' | wc -l

#6. length of shortest word
echo "6.the shortest word length is: "
awk '{print length , $0}' words | sort -n | cut -d " " -f2- | head -1 | wc -c

#7. length of the longest word 
echo "7.the longest word Length is: "
awk '{print length, $0 }' words | sort -n | cut -d " " -f2- | tail -1 | wc -c

#8. how many words in word file with only words having 4 and 5 letters
echo "8.number of words with only 4 and 5 letters: "
grep -x '.\{4,5\}' words | wc -l

#9. number of bytes for output of solution 8
echo "9.number of bytes from solution 8: "
grep -x '.\{4,5\}' words | wc -c

#10. number of processes in processes.txt
echo "10.number of processes in processes.txt file: "
wc -l processes.txt

#11. how many processes listed in procces do not belong to root
echo "11.number of processes that are not root: "
cat processes.txt | grep -v 'root' | wc -l

#12. process id of ssh daemon
echo "12.process id of ssh Daemon: "
cat processes.txt | grep 'ssh'

# 13. parent process name of ssh daemon
echo "13.parent process of ssh daemon : "
ps 1 

#14. number of interactive logon sessions
echo "14.number of interactive logon sessions tty: "
cat processes.txt | grep 'tty' | wc -l

#15. sum up total process ids
echo "15.the sum total of process ids is: "
awk '{s+=$2}END{print s}' processes.txt
