#/home/does/EN!
#
# TITEL :Data Decryption Algorithm 
#AUTHOR : Bhushan makan patil <patilbhushan8595@gmail.com>
#
#
#
###################################################################################
import os ,sys ,time 
###################################################################################
class Data_Decryption(object):
	def __init__ (self,file):
		self.file_name=file
		#self.dir_=directory
		self.process()

	def process(self):
		self.get_Decrypt()
		print('ok....')
		self.put_in_Defile()
		


	def get_Decrypt(self):
		try:
			print('[_**~~ ] key process .......')
			data_key=[]
			data_key=[chr(ord(i)-int(open(os.getcwd()+'/key_encrypt','r').read()[91:93])) for i in \
			open(os.getcwd()+'/key.bin','r').read()[624:626]]
			self.Dec_file_data=[chr(ord(i) -int(data_key[0]+data_key[1])) for i in open(os.getcwd()+'/'+self.file_name,'r').read() ]
			print('[_**~~ ] key process complete......')
		except Exception as e :
			print(e)
	def put_in_Defile(self):
		try :
			with open(os.getcwd()+'/'+self.file_name , 'w') as file :
				for i in self.Dec_file_data :
					file.write(i)
				file.close()
			print('process complet.....')
		except Exception as e :
			print('[___**___]',e)


#########################################################################################
#int(open('key.bin','r').read()[1136:1138])
#91
#>>> int(open('key.bin','r').read()[1139:1142])
#93
x=Data_Decryption('EncData_2')

