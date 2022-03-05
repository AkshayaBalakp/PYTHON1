import csv
f=open("Fruit.csv","w")
writer=csv.DictWriter(f,fieldnames=["fruit","count"])
writer.writeheader()
writer.writerow({"fruit":"manogo","count":"1"})
writer.writerow({"fruit":"apple","count":"2"})
f.close()
c=0
f=open("Fruit.csv")
reader=csv.DictReader(f)
for row in reader:
    if c==0:
        print(f'{"".join(row)}')
        print({row["fruit"]},{row["count"]})
f.close()