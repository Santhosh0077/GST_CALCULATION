item=input("enter item name:")
price=float(input("enter the price of the item:"))
print('---------INVOICE---------')
if price<10000:
    gst=5
elif price>1000 and price<50000:
    gst=12
else :
    gst = 25
gst_amount=(price * gst)/100
net_amout=(gst_amount + price)
print(f'ITEM NAME={item}')
print(f'PRICE ={price}')
print(f'GST is {gst}%')
print(f'GST AMOUNT={gst_amount}')
print(f'Net AMOUNT={net_amout}')
