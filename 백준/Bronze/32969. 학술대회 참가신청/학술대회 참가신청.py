a = ["social", "history", "language", "literacy"]

temp = input().lower()
for element in a:
    if temp.find(element) != -1:
         print("digital humanities")
         break
else: print("public bigdata")
