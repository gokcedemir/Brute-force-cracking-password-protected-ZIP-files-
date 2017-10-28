##########################################################
# 19.10.2017 - CTF cozumunde yazildi
# Brute force ile zip'in parolasini bulma. 
# 2000 ile 2250 arasinda bir sayi oldugu bilinen parolayi bulup zip'i acma.
#gtd

from zipfile import ZipFile
for i in range(2000,2250):
	try:
		a=ZipFile("konum.zip")    # zip'in adi verilir
		a.extractall(pwd=str(i).encode())
		print(i)                 
	except:
		pass
