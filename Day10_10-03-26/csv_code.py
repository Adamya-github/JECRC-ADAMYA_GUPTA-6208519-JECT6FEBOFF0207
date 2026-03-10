import csv
from datetime import date

file = open('expense.csv', 'a+', newline='')

w = csv.writer(file)
r = csv.reader(file)

# w.writerow([   ## Columns
#   'DATE',
#   'CATEGORY',
#   'AMOUNT'  
# ])
# w.writerows( ## Rows
#   [
#     [date.today(), 'Travel', 2000],
#     [date.today(), 'Food', 550],
#     [date.today(), 'Entertainment', 1700]
#   ]
# )

file.seek(0)
print(list(r))

file.close()