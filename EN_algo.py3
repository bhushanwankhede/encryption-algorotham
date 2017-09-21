#/home/does/EN!
#
# TITEL :Data Encryption Algorithm 
#AUTHOR : Bhushan makan patil <patilbhushan8595@gmail.com>
#
#
#
#########################################################################################################
import os 
import sys
import time 
############################################################################################################
class Data_Encryption(object):
	def __init__(self,directory ):
		self.dir_=directory
		self.read_file_1()
		self.process()

	def read_file_1(self):
		try :
			with open(self.dir_, 'r+',encoding='utf-8') as file_1 :
				self.file_data=file_1.read()
				file_1.close()
				print('[ * ] read file successfully..... ' )
		except Exception as e :
			self.file_data='bhushan'
			print('[ERROR] ' ,e)
	def process(self):
		self.get_key()
		self.get_ord()
		self.put_key()
		self.get_enc_chr()
		self.put_in_file()
	
	def get_key(self):
		try:
			print('[_**~~ ] key process .......')
			self.key=[chr(ord(i)-int(open(os.getcwd()+'/key_encrypt','r').read()[91:93])) for i in \
			open(os.getcwd()+'/key.bin','r').read()[624:626]]
			print('[_**~~ ] key process complete......')
		except Exception as e :
			print(e)
		
	def get_ord(self):
		print('[ _*_ ] Start conversion......')
		self.ord_data=[ord(i) for i in self.file_data ]
		print('[ _*_ ] Conversion complete....')
	
	def put_key(self):
		print('[ __*__ ] Start put key......')
		self.key_put_data=[i+int(self.key[0]+self.key[1]) for i in self.ord_data]
		print('[ __*__ ] Put key complete.....')

	def get_enc_chr(self):
		print('[ ___*___ ] Start conversion of En char.......')
		self.enc_data=[chr(i) for i in self.key_put_data]
		print('[ ___*___ ] Enc chr conversion complete ' )

	def put_in_file(self):
		try :
			#file_number=int(open(os.getcwd()+'/k','r',encoding='utf-8').read()[3])
			print('[ ____*____ ] Start Data write in file...... ')
			with open(os.getcwd()+self.file_name , 'a+') as file_2:
				for i in self.enc_data :
					file_2.write(i)
				file_2.close()
			print('[ ____*____ ]  Data Encryption is done ')
		except Exception as e:
			print('[ ____*____] Data Encryption error ',e)
				
			
#################################################################################################################################

print('Start  Time : ',time.strftime('%d/%m/%y  %I : %M : %S %P ' , time.localtime(time.time())))
d=Data_Encryption(r'/home/bhushan/Downloads/Grammerer/Data/TheYellowWallpaper.txt')
print('End Time : ',time.strftime('%d/%m/%y %I : %M : %S %P' ,time.localtime(time.time())))
