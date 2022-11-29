# 1)for loop
# 2)while loop

# i-საიტერაციო ცვლადი

# for i in range ("giorgi"):          #range(7) = (0,1,2,3,4,5,6)
#     print("nika")

#             #start,finish,step
# for x in range (3,6,2):      #range(3,6) = 3,4,5
#     print(str(x) + "nika")


# i = 0   #საიტერაციო ცვლადი
# while i < 5:
#     print("nika")
#     print(i)
#     i += 1    #3 საიტერაციო ცვლადის ინკრემენტაცია
    

# full_name = "tornike suarishvili"

# i = 0  #საიტერაციო ცვლადი

# while i < 5:
#     print ("tornike suarishvili")
#     print(i)
#     i += 1     # საიტერაციო ცვლადის ინკრემენტაცია

# i = 0

# while i < len(full_name):
#     print(full_name[i])
#     i += 1


# a = "qwerty"
# b = "asdfgh"


# i = 0   # საიტერაციო ცვლადის შემოტანა

# while i < len(a):
#     print(a[i] + b [i])
#     i += 1 




# Homework

# ინპუთით შეიტანეთ თქვენი სახელი და გვარი
# ტერმინალში გამოოიტანეთ რომელ ინდექსებზე არის ხმოვნები


full_name = input("enter your name: ")

i = 0

while i < len(full_name):
    if full_name[i] in "aeiou":
        print(str(i) + "  " + full_name[i])
    i += 1






















