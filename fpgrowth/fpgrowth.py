from fpgrowth_py import fpgrowth
import pandas

df = pandas.read_excel('./dataset/Online Retail 1.xlsx', sheet_name='Online Retail')

mylist = []
buff = []
trans = df['InvoiceNo'].unique().tolist()
products = df['Description'].tolist()
alltrans = df['InvoiceNo'].tolist()
counter = 0

for i in range(len(trans)-1):
    while(alltrans[counter] == trans[i]):
        buff.append(products[counter])
        counter += 1
    mylist.append(buff)
    buff=[]

freqItemSet, rules = fpgrowth(mylist, minSupRatio = 0.05, minConf = 0.6)
i = 1
for item in rules:
    print(i, end = '. ')
    print(item, end = ',\n')
    i += 1