# n = int(input()) # number of products

# price_each_products = list(map(int, input().split())) # price of each product

# distance = list(map(int, input().split())) # shipping distance for each product from fulfillment center in 00's km means 1 = 100km(centurion km)

# sku = list(map(int, input().split())) # fulfillments available stocks (if the stock is negative then the stock is overpurchased...product is not available and cannot be shipped to the customer) 


# for i in range(n):
# 	if sku[i] > 0:
# 		print(price_each_products[i] * distance[i], end=" ") #price available would further increase by factor distance. The price on for each product varies based on the distance of the customer from the fulfillment center



rows, cols = map(int, input().split())

maximum = 0
rowno = 0
for i in range(rows):
	sumcols = sum(list(map(int, input().split())))
	print("Row"+str(i+1)+":",sumcols)
	if maximum < sumcols:
		maximum = sumcols
		rowno = i+1

print("Row"+str(rowno)+":", maximum)
