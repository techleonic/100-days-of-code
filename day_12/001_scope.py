
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
print(enemies)

while True: #you can get the variable inside a while an if
  n1 = 2
  break

print(n1)

#local and global variables.
enemies = 1 

def increase_enemies ():
  #enemies +=1 you can not access a variable Global variable in a local context directly
  global enemies
  enemies +=1
  print(enemies)

def enemies_plus():
  return enemies+1 # when you use the keyword return you ar able to use goblal variables

increase_enemies()
print(enemies)
print(enemies_plus())