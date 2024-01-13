import json #to read and write json file with to do list 


#declaring a global vairable to handle to do list
global To_Do_List 
To_Do_List=[]

#list in json file is stored in "To_Do_List"
with open('ToDoList.json') as Read_f:
    To_Do_List= json.load(Read_f)
    
#Creat new list with new name
if len(To_Do_List)==0:    
     name=input("Enter the name of list:")
     To_Do_List.append(f"{name} To Do List")
 
 #Function to exit Application   
def Exit():
  with open("ToDoList.json","w") as Write_f:
          json.dump(To_Do_List,Write_f)
          print("Exit")

#Main Menu of Application
while True:
    try: #handle the application if invalid operation is done 
      print("To Do List")
      print("Select 1 to Add")
      print("Select 2 to Remove an item")
      print("Select 3 to Update an item")
      print("Select 4 to Show list")
      print("Select 5 to Check")
      print("Select 6 to clean the list and exit")
      print("Select 7 to exit")
    
      choose = input("Enter an Option:")
   
   #Items are added to list from here
      if choose=='1':
        x = input("Enter Desciption of list:")
        To_Do_List.append(f"• {x}")
    
    #Items are removed in list from here 
      elif choose=='2':
        print("\n")
        print(*[item for item in To_Do_List],sep='\n')
        print("\n")
        num = input("Enter item No. to be removed:")
        num = int(num)
        To_Do_List.pop(num)
    
    #Items in list can be updated from here     
      elif choose=='3':
       num= input("Enter item No. to be updated:")
       num= int (num)
       New_Task=input("Enter Task:")
       To_Do_List[num]=f"• {New_Task}"
       print("Task is updates")
    
    #List can be displayed from here  
      elif choose=='4':
        print("\n")
        print(*[item for item in To_Do_List],sep='\n')
        print("\n")
    
    #Items can be checked from here
      elif choose=='5':
        num = input("Enter item to be checked:")
        num=int(num)
        To_Do_List[num]+=" ✅"
    
    #Clean the list and exit  
      elif choose=='6':
        To_Do_List.clear()
        print("List is cleaned")
        Exit()
        break
    #To do list application can be closed from here       
      elif choose=='7':
        #before exiting list is saved to json file
        Exit()
        break
    #handle the programme if invalid entry is been done 
      else:
        print("Invalid Option")
    except Exception:
      print("Invalid operation performed")