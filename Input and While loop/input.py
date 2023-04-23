print("What is your name?", end=" ")
name = input()
print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print("%s, you're %s old, %s tall and %s heavy." %(name, age, height, weight))

country = input("Which country are you from?: ")
feelings = input("Express how you're feeling today in one word?: ")
print("%s, You are from %s and you are feeling %s today" % (name, country, feelings))