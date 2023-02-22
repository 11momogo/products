# while 迴圈比 for 迴圈更適合用於無限次的輸入

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

products[0][0]