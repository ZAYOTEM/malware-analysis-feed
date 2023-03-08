import sys
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
key = "850c61ff7cfc4c28ae073b6ce7172cbd850c61ff7cfc4c28ae073b6ce7172cbd850c61ff7cfc4c28ae073b6ce7172cbd850c61ff7cfc4c28ae073b6ce7172cbd"  #850c61ff7cfc4c28ae073b6ce7172cbd
#word = "IQK6UMS6 Iqx5pssbKaf7TwA3SRr5IWC8Q3wUMVlHW4r5ILdIk=="

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

alphabet1 = alphabet[::-1]

for line in lines:
    final = ""
    counter=0
    
    while(len(line)!= counter+1 and line[counter]!="="):
        indexAlp= 0
        while(alphabet1[indexAlp] != key[counter]):
            indexAlp+=1

        indexAlp2 = 0
        print(line[counter])
        while(alphabet[indexAlp2] != line[counter]):
            indexAlp2+=1

        final +=alphabet[((indexAlp+1) + (indexAlp2+1)) % 63 -1]
        counter +=1   
    text_file = open("cozum2.txt", "a")    
    text_file.write(final+"\n")
    text_file.close()

