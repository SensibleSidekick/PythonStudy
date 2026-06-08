user_search = input("What acronym do you want to look for?\n")

found = False
with open('input.txt') as file:
   for line in file:
      if user_search in line:
         print(line)
         found = True
         break
      
if not found:
   print('The acronym does not exist')



