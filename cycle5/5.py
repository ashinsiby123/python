import csv
field_name = ['No', 'Company', 'Car Model']
car = [{'No': 1,'Company':'Ferrari','Car Model':'GH'}]
with open('b.csv', 'w') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('b.csv', newline='') as csvfile:
   d = csv.reader(csvfile, delimiter='|')
   for r in d:
    print(','.join(r))
