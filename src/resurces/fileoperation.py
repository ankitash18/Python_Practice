import os

b= os.listdir('C:\\Users\\AShrivastava\\Desktop\\Documents\\Ankita')

a= os.path.exists('C:\\Windows\\System32\\calc.exe')

print(a)

print(b)

totalsize =0
for filename in os.listdir('C:\\Users\\AShrivastava\\Desktop\\Documents\\Ankita'):
        if os.path.isfile(os.path.join('C:\\Users\\AShrivastava\\Desktop\\Documents\\Ankita',filename)):
            print(filename)


hellofile = open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\hello.txt')

#content = hellofile.read()

content1 = hellofile.readlines() #return list
print(content1)

hellofile.close()


hellofile1 = open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\hello.txt','a')

hellofile1.write('hello!!!!!!!!!!!')


hellofile1.close()

print(os.getcwd())


import shelve #to store data as dictonariy in file

#shelfile = shelve.open('C:\\Users\\AShrivastava\\Desktop \\study\\sparkrockthejvm\\python\\shelve.txt','w')

#shelfile['cat'] =['a','b','c','d','e']

#shelfile.close()

#shelfile = shelve.open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\shelve.txt')

#a = shelfile['cat']

#print(a)


import shutil #copy file

shutil.copy('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\hello.txt','C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\shelve.txt')



#copytree - copy entire folder
#move file  - move
#os.unlin - delete the file
#shutil - rmtree - remove entire folder n its contents


os.chdir('C:\\Users\\AShrivastava\\Downloads')

for filename in os.listdir():
    if filename.endswith('.ica'):
        print(filename)
        #os.unlink(filename)