import csv

with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\airtravel.csv','r') as f:
    reader = csv.reader(f)  #reader is an pbject and is iterable
    next(reader)
    year_1958 =dict()
    for row in reader:
        #print(row)
       # print(row[1])
        year_1958[row[0]] = row[1]

    #print(year_1958)

    max_1958 = max(year_1958.values())

    #print(max_1958)

    for k,v in year_1958.items():
        if max_1958 == v:
            print(f'busy month is {k} and value is {v.strip()}')





#wirtin csv file

with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\people.csv','a') as f:
    wrtier = csv.writer(f)
    csvdata = (5,'Anne','Amsterdam')
    wrtier.writerow(csvdata)


with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\numbers.csv','w',newline ='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','x**2','x**3','x**4'])
    for x in range(1,10):
        writer.writerow([x, x**2, x**3, x**4])


with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\passwd.csv','r') as f:
    reader = csv.reader(f,delimiter =':',lineterminator='\n')
    for row in reader:
        print(row)









