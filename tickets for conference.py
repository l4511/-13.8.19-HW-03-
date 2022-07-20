print("hello")
print("how many ticket you want?")
ticket_quantity = input("quantity = ")
print("ok")
print(ticket_quantity)
total_price = 0
ticket = 0
for ticket in range(int(ticket_quantity)):
	ticket += 1
	print("how many old are you?")
	age = input("age ")
	if int(age) < 18 : 
		print("for child ticket free")
	elif 18 < int(age) < 25 :
		print("ticket price is 990 rub")
		total_price = int(total_price) + 990
	else :
		print("ticket price is 1390 rub")
		total_price = int(total_price) + 1390
if int(ticket_quantity) > 3 :
	print("you have discount")
	total_price = total_price - total_price*10/100
print("price is" , total_price , "rub")