from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")
bidders = []
other_bidders = "yes"
while other_bidders == "yes":
    name = input("What is your name? ")
    bid =  int(input("What's your bid $"))
    bidders_dict = {"name":name, "bid":bid}
    bidders.append(bidders_dict)
    other_bidders = input("Are ther any other bidders? Type 'yes' or 'no' ")
    if other_bidders == "yes":
        clear()

clear()
highest_bed = 0
highest_bed_index =0
for  i in range(len(bidders)):
    if highest_bed > bidders[i]["bid"]:
        highest_bed = bidders[i]["bid"]
        highest_bed_index = i
    else:
        
        continue

print(f"The winner is {bidders[highest_bed_index]["name"]} with a bid of  ${bidders[highest_bed_index]["bid"]}")
