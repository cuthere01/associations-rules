from efficient_apriori import apriori
import pandas

# Чтение данных из файла Excel
df = pandas.read_excel('./dataset/Online Retail 1.xlsx', sheet_name='Online Retail')

# Подготовка данных
mylist = []
buff = []
trans = df['InvoiceNo'].unique().tolist()
products = df['Description'].tolist()
alltrans = df['InvoiceNo'].tolist()
counter = 0

# Построение списка транзакций
for i in range(len(trans)):
    while counter < len(alltrans) and alltrans[counter] == trans[i]:
        buff.append(products[counter])
        counter += 1
    if buff:  # Проверяем, чтобы buff не был пустым
        mylist.append(buff)
    buff = []

# Убедимся, что список транзакций не содержит пустых списков
mylist = [transaction for transaction in mylist if transaction]

# Применение алгоритма Apriori
itemsets, rules = apriori(mylist, min_support=0.05, min_confidence=0.6)

# Вывод ассоциативных правил
i = 1
for item in rules:
    print(i, end='. ')
    print(item, end=',\n')
    i += 1
