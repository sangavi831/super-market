import smtplib
import datetime
def vegetables():
   onion_kg=20
   tomato_kg=15
   potato_kg=10
   
   custumer_buy=input("enter vegetables you buy:")
   if custumer_buy=="onion":
     quantity=int(input("enter quantity in kg:"))
     amount=onion_kg*quantity
     f=open("bill.txt","a")
     f.write(f'your bill is{amount}')
     print("bill generated")
     cont=input("do you want to continue to buy vegetables:")
     if cont=="yes":
        vegetables()
     else:
       print("thank you")
     nxt_sele=input("do you want to continue with next selection:")
     if nxt_sele=="yes":
        main()
     else:
        print("thank you for shopping")
   elif custumer_buy=="tomato":
      quantity=int(input("enter quantity:"))
      amount=tomato_kg*quantity
      f=open("bill.txt","a")
      f.write(f'your bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy vegetables:")
      if cont=="yes":
        vegetables()
      else:
       print("thank you")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")

   elif custumer_buy=="potato":
      quantity=int(input("enter quantity:"))
      amount=potato_kg*quantity
      f=open("bill.txt","w")
      f.write(f'your bill potato is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy vegetables:")
      if cont=="yes":
        vegetables()
      else:
        print("thank you")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
  
   else:
       print(f"your{custumer_buy}is not available")
def fruits():
    custumer_buy=input("enter fruits you buy:") 
    apple_kg=80
    orange_kg=35
    watermelon_kg=70
    mango_kg=100
    if custumer_buy=="apple":
     quantity=int(input("enter quantity in kg:"))
     amount=apple_kg*quantity
     f=open("bill.txt","w")
     f.write(f'your apple bill is{amount}')
     print("bill generated")
     cont=input("do you want to continue to buy fruits:")
     if cont=="yes":
        fruits()
     else:
      print("thank you ")
     nxt_sele=input("do you want to continue with next selection:")
     if nxt_sele=="yes":
        main()
     else:
        print("thank you for shopping")
    elif custumer_buy=="orange":
      quantity=int(input("enter quantity in kg:"))
      amount=orange_kg*quantity
      f=open("bill.txt","w")
      f.write(f'your orange bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy fruits:")
      if cont=="yes":
        fruits()
      else:
       print("thank you ")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
            

    elif custumer_buy=="watermelon":
      quantity=int(input("enter quantity in kg:"))
      amount=watermelon_kg*quantity
      f=open("bill.txt","w")
      f.write(f'your  watermelon bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy fruits:")
      if cont=="yes":
        fruits()
      else:
        print("thank you")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
       
    elif custumer_buy=="mango":
      quantity=int(input("enter quantity in kg:"))
      amount=mango_kg*quantity
      f=open("bill.txt","w")
      f.write(f'your mango bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy fruits:")
      if cont=="yes":
        fruits()
      else:
        print("thank you ")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
    else:
      print(f"your{custumer_buy}is not available")
def snacks():
   custumer_buy=input("enter snacks you buy:") 
   chips=20
   chocolates=35
   softdrinks=30
   icecreams=40
   if custumer_buy=="chips":
     quantity=int(input("enter quantity:"))
     amount=chips*quantity
     f=open("bill.txt","w")
     f.write(f'your chips bill is{amount}')
     print("bill generated")
     cont=input("do you want to continue to buy snacks:")
     if cont=="yes":
        snacks()
     else:
      print("thank you ")
     nxt_sele=input("do you want to continue with next selection:")
     if nxt_sele=="yes":
        main()
     else:
        print("thank you for shopping")
   elif custumer_buy=="chocolates":
      quantity=int(input("enter quantity:"))
      amount=chocolates*quantity
      f=open("bill.txt","w")
      f.write(f'your chocolates bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy snacks:")
      if cont=="yes":
        snacks()
      else:
        print("thank you")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
   elif custumer_buy=="softdrinks":
      quantity=int(input("enter quantity:"))
      amount=softdrinks*quantity
      f=open("bill.txt","w")
      f.write(f'your softdrink bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy snacks:")
      if cont=="yes":
        snacks()
      else:
        print("thank you ")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
   elif custumer_buy=="icecreams":
      quantity=int(input("enter quantity:"))
      amount=icecreams*quantity
      f=open("bill.txt","w")
      f.write(f'your icecream bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy snacks:")
      if cont=="yes":
        snacks()
      else:
        print("thank you ")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
   else:
      print(f"your{custumer_buy}is not available")
def households():
   custumer_buy=input("enter households you buy:") 
   masalas=30
   washing_things=100
   allpurposeflour=60
   cleaning_things=70
   if custumer_buy=="masalas":
     quantity=int(input("enter quantity:"))
     amount=masalas*quantity
     f=open("bill.txt","w")
     f.write(f'your masalas bill is{amount}')
     print("bill generated")
     cont=input("do you want to continue to buy households:")
     if cont=="yes":
        households()
     else:
        print("thank you")
     nxt_sele=input("do you want to continue with next selection:")
     if nxt_sele=="yes":
        main()
     else:
        print("thank you for shopping")
   elif custumer_buy=="washing_things":
      quantity=int(input("enter quantity:"))
      amount=washing_things*quantity
      f=open("bill.txt","w")
      f.write(f'your  washing things bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy households:")
      if cont=="yes":
        households()
      else:
        print("thank you")
        nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
   elif custumer_buy=="allpurposeflour":
      quantity=int(input("enter quantity:"))
      amount=allpurposeflour*quantity
      f=open("bill.txt","w")
      f.write(f'your flour bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy households:")
      if cont=="yes":
        households()
      else:
        print("thank you")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
   elif custumer_buy=="cleaningthings":
      quantity=int(input("enter quantity:"))
      amount=cleaning_things*quantity
      f=open("bill.txt","w")
      f.write(f'your cleanig things bill is{amount}')
      print("bill generated")
      cont=input("do you want to continue to buy households:")
      if cont=="yes":
        households()
      else:
        print("thank you")
      nxt_sele=input("do you want to continue with next selection:")
      if nxt_sele=="yes":
        main()
      else:
        print("thank you for shopping")
   else:
      print(f"your{custumer_buy}is not available")
def main():
  section_select=input("enter section:")
  if section_select=="vegetables":
      vegetables()
  elif section_select =="fruits":
     fruits()
  elif section_select=="snacks":
    snacks()
  elif section_select=="households":
   households()
  else:
    print("thank you for shopping")
def emailsending():
 try:
  receiver_mails=["lokeshwaribhavani3@gmail.com"]
  for i in receiver_mails:
   f=open("bill.txt","r")
   txt=f.read()
   print(i,txt)
   x=datetime.datetime.now()
   print(i,x)
   s=smtplib.SMTP('smtp.gmail.com',587)
   s.starttls()
   s.login("sangavis831@gmail.com","bash tzfe sswi msra")
   message=(f"your total amount is {txt}{x}\n\nthank you and visit again!")
   s.sendmail("sangavis831@gmail.com",i,message)
   s.quit()
   print("mail sent sucessfully")
 except:
   print("not sent")

