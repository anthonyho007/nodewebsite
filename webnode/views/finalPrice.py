def finalPrice(prices):
	n = len(prices)
	discountMap = {}
	for i in range(n):
		for j in range(i+1, n):
			if prices[j] <= prices[i]:
				if i not in discountMap:
					discountMap[i] = prices[j]
	return discountMap

A= [6,5,1,3,4,6,2]
print (finalPrice(A))

