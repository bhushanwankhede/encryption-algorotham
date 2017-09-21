                            


with open('key.bin','r') as file :
	key_data=file.read()
	file.close()


ord_data=[ord(i)+int(open('key_encrypt','r').read()[91:93]) for i in key_data]
chr_data=[chr(i) for i in ord_data ]

with open('key.bin','w') as file :
	for i in chr_data:
		file.write(i)

	file.close()

for i in chr_data:
	print(i,end='')




	





