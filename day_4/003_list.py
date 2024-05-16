#list

states_of_america = ["Deleware","Pennsylvania",]

#list have a order. an starts with 0
print(states_of_america[0])

#last item
print(states_of_america[-1])

#modified list
states_of_america[-1] = "Pencilvania"
print(states_of_america)

#add item to a list
states_of_america.append("Lioland")
print(states_of_america)

#Adding a list to a list
states_of_america.extend(["Danialan","Kenialand"])
print(states_of_america)