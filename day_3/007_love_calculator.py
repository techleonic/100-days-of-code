name1 =  input("Enter name one: ").lower().strip()
name2 = input("Enter name two: ").lower().strip()

names = name1 + name2
true_count = 0
love_count = 0
total = ""
for i in names:
    if i in "true":
        true_count+=1
    if i in "love":
        love_count+=1
total = int(str(true_count)+ str(love_count))
print(f"your score is : {total}")


if  total <= 10 or total >= 90:
    print("you go together like coke and mentos")
elif total >= 40 and total <= 50:
    print("you go together very well")
else:
    pass 