end = 0x433E59 	# Here is for end of the encoded string's
start = 0x4333F0	# Start of encoded string's address
value = idaapi.get_bytes(start,end-start)
stringValue = value.decode("utf-8")
listedValue = stringValue.split('\x00')


def yaz(final):
	if(final != ""):
		text_file = open("Decrypted.txt", "a")    
		text_file.write(final+"\n")
		text_file.close()

def decodeToBase64(listedValue):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    key = "850c61ff7cfc4c28ae073b6ce7172cbd850c61ff7cfc4c28ae073b6ce7172cbd850c61ff7cfc4c28ae073b6ce7172cbd850c61ff7cfc4c28ae073b6ce7172cbd"  #850c61ff7cfc4c28ae073b6ce7172cbd
    alphabet1 = alphabet[::-1]
	
    for line in listedValue:
        final = ""
        counter=0
        while(len(line)!= counter and line[counter]!="=" and line[counter]!="+"):
            indexAlp= 0
            while(alphabet1[indexAlp] != key[counter]):
                indexAlp+=1
            indexAlp2 = 0
            #print(line[counter])
            while(alphabet[indexAlp2] != line[counter]):
                indexAlp2+=1

            final +=alphabet[((indexAlp+1) + (indexAlp2+1)) % 63 -1]
            counter +=1
        yaz(final)
decodeToBase64(listedValue)
			

			
