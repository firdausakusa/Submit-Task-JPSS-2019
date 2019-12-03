#TUGAS

'''

1. Buatlah program untuk membaca dan menampilkan kalimat - kalimat pada 
file abstrak.txt seperti pada gambar berikut pada console monitor
2. Buatlah program untuk menyimpan hasil pembacaan no 1 (seperti pada gambar) 
ke dalam file bernama potongan_abstrak.txt pada direktori yang bernama 
"nama anda", direktori tersebut juga anda buat langsung dari program
3. Sama seperti nomor 2 akan tetapi file disimpan dalam format 
potongan_abstrak.ser


1. Read
2. Write
3. Serialisasi (terenskripsi)--> Library import bytes
pickle.dump---> writing dalam bentuk serial atau deserial
readfile, writefile
setelah read dan write, sebelumnya buat directory

with open('E:/Class/abstract.txt', 'r') as file_handling: 
    gonesinau_text = file_handling.read()
    print(gonesinau_text)

import os
os.mkdir(E:/Class/)
#serelization
import Bytes10 #import libraries
readfile=Bytes10() #reading file
pickle.dump(readfile, witefile) #writefile
'''

#1
openfile = open ('E:/Class/abstract.txt', 'r')
reading = openfile.seek(80)
reading = openfile.read()
print(reading)

#2
import os
try:
    os.mkdr('E:/Class/firdausa)

except FileExistsError:
    pass

fileHandle_write = open('E:/Class/potongan_abstrak.txt', 'w')
fileHandle_write.write(reading)
filehandle_write.close()

#3
import pickle
from io import Bytes10()

#read file potongan.abstract.txt
readfile = open ('E:/Class/potongan_abstrak.txt', 'r')
readfile = readingfile.read()

#write file potongan.abstract.ser
writingfile = open('E:/Class/potongan_abstrak.ser', 'wb')

#converting an obyek in memory to a byte stream (from potongan_abstract.txt to potongan_abstract.ser)
pickle.dump(readfile, writingfile)

readingfile.close()
writingfile.close()

#Show the original pickle file
print('\nShow the original pickle file')

#Show the result of converting the pickled file
picklefile = open('E:/Class/potongan_abstrak.ser', rb)
data = pickle.load(picklefile)
picklefile.close()
print('\n Showing Result of Converting the Pickle\n ')