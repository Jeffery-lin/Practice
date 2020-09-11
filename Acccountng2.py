#讀取檔案
product = []
with open('product.csv', 'r') as f:
	for line in f:
		if '商品名稱,金額' in line:#若讀取到檔案內的商品名稱與金額的字串
			continue#跳到下一回，表示讀取的這行我不做處理，直接跳下一行(迴)繼續
		line.split(',')
		#s = line.strip().split(',')
		name, price = line.strip().split(',')#檔案中有一個逗點，表示此清單有兩個變數，把該檔案的內容分別丟到name與price
		product.append([name, price])#把name與price當作一個小清單加入到另一個大清單
		#print(name)
		#print(price)
print(product)
#讓使用者輸入
total_price = 0
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	product.append([name, price])
	total_price += price
print (product)
print ('輸入的總額是是', total_price)

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('product.csv', 'w') as f:
	f.write('商品名稱,金額\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')