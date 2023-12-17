item=input("enter item name:")
price=float(input("enter the price of the item:"))
print('---------invoice---------')
if price<10000:
    gst=5
elif price>1000 and price<50000:
    gst=12
else :
    gst = 25
gst_amount=(price * gst)/100
net_amout=(gst_amount + price)
print(f'item name={item}')
print(f'price ={price}')
print(f'gst is {gst}%')
print(f'gst amount={gst_amount}')
print(f'net_amount={net_amout}')
