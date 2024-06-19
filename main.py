import products
import datetime
print("***ss super market***")
print("supermarket blueprint***")
section=['vegetables-> a1','fruits->a2','beverages->a3','snacks->a4','cleaning&household->b1','beauty&hygiene->b2','homekitchen->b3']
for i in section:
    print(i)
x=datetime.datetime.now()
print(x)
try:

 custumer_buy=input("enter selection:") 
 if custumer_buy=="vegetables":
   products.vegetables()
   
  
 elif custumer_buy=="fruits":
    products.fruits()
    
 elif custumer_buy=="snacks":
   products.snacks()
   
 elif custumer_buy=="households":
   products.households()

 products.emailsending()   
except:
  print("please select properly!")   

   




  