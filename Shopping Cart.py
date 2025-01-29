'''5. Shopping Cart
   - Create a program to simulate a shopping cart:
     - Add items (item name and price).
     - View cart items.
     - Calculate the total price.
     - Exit.
   - Use functions and a loop to allow multiple actions.'''

def get_inputs(total_price):
   while True:
      option=int(input('choose a option:\n1.Add items \n2.View Cart \n3.Calculate total price \n4.Exit \n'))
      if option==1:
         item_name,item_price=add_items()
      # elif option==2:
      #    cart_items=view_cart(item_name)
      elif option==3:
         final_price=calculation(total_price,item_price)
         print(f'The total price for the items in the cart is {final_price}')
      else:
         break
def add_items():
   item_name=input('enter the item name: ')
   item_price=int(input('enter the item price: '))
   if item_price<0:
      item_price=int(input('enter valid item price: '))
   return item_name,item_price
def calculation(total_price,item_price):
   total_price += item_price
   return total_price
# def view_cart(item_name):
#    return vi
def main():
   print('welcome to sp mart')
   total_price=0
   option=get_inputs(int(total_price))
main()