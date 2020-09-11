product = []
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
for p in product:
	print(p[0], '的價格是', p[1])

with open('product.csv', 'w') as f:
	f.write('商品名稱,金額\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')