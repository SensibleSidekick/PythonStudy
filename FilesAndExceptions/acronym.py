def find_acronym():
   user_search = input("What acronym do you want to look for?\n")

   found = False
   try:
      with open('input.txt') as file:
         for line in file:
            if user_search in line:
               print(line)
               found = True
               break
   except FileNotFoundError as e:
      print("File Not Found")
      return  
      
      
   if not found:
      print('The acronym does not exist')

   

def add_acronym():
   acronym = input("What acronym do you want to add?\n")
   definition = input ("What is the definition?\n")

   with open('input.txt', 'a') as file:
      file.write(acronym + ' - ' + definition + '\n')

def main():
   choice = input("Do you want to find (F) or add (A) an acronym?")
   
   if choice == "A":
      add_acronym()
   elif choice == "F":
      find_acronym()
   else:
      print("Option not applicable")

main()