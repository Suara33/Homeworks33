

               #HOMEWORK



# my_list = ("xinkali", "mwvadi", "lobiani", "qababi", "xachapuri", "cyali")

# prices = (2, 20, 15, 13, 16, 2)


# xinkali girs 2 lari
# mwvadi girs 20 lari

# my_list = ("xinkali", "mwvadi", "lobiani", "qababi", "xachapuri", "cyali")

# prices = (2, 20, 15, 13, 16, 2)

# i = 0    საიტერაციო ცვლადი
# while i < len(my_list):
#     print(my_list[i] +" "+"girs"+" "+str(prices[i]) +" "+"lari")
#     i +=1


#--------------------------------------------------------------------------------------------------



# my_arr = ["banana", "true", 5, "tornike", 10.5, [1,2,3], 5, 10]

# კვადრატული ფრჩხილით შექმნილი კოლექცია არის list-ი.

# print(my_arr[1])

# print(my_arr[0])

# print(my_arr[-2])

# print(my_arr[1:5:2]) 







# მომხმარებელს შემოატანინეთ 5 საჭმელი,
# სიაში შეიტანეთ ისინი რომლებიც შეიცავენ 2 "ა"-ს.

# food1 = input("enter food1: ")
# food2 = input("enter food2: ")
# food3 = input("enter food3: ")


# menu = []
# i = 0
# for i in range(3):
#     food = input("enter your food: ")
#     for char in food:
#         if char == "a":
#                print(food)
#     i +=1




# menu.remove("cyali")

# menu.remove("qababi")

# del (menu[2])

# print(menu)

# წაშალეთ ის ელემენტები რომლებშიც მეორე ასო არის "ა"

# menu = ["xinakli", "mwvadi", "xachapuri", "soko", "kartofili", "qababi"]
# new_menu = []
# for food in menu:
#     if food[1] !="a":
#         new_menu.append(food)
# print(new_menu)


# scores = [10,87,9,25,89,33,77,99,82,4,7]

# scores.sort()

# print(scores)

#                                       homework

# 1)დამიპრინტეთ  scores = [10,87,9,25,89,33,77,99,82,4,7]

# sort მეთოდის და max მეთოდის ფუნქციის გამოყენების გარეშე დამიბრუნეთ ყველაზე დიდი რიცხვი


# 2) while ციკლით სათითაოდ შეამოწმეთ ელემენტი და მის მარჯვნივ მდგომი,

# რომელიც უფრო დიდი იქნება,დროებით მიანიჭეთ მაქსიმუმის მნიშვნელობა და შემდეგ 

# შეადარეთ მის მარჯვნივ მდგომს.


# 3) students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]

# შეატრიალეთ უკუღმა sort და  revers-ის გარეშე


scores = [10,87,9,25,89,33,77,99,82,4,7]


# 1) print(max(scores))


# 2)sort

scores.sort()

print(scores)

print(scores[-1])

# name = "nikax"
# scores=[20,43,5,97,73]

# # n-20
# # i-43
# # k-5

# i = 0

# while i < len(name):
#     print(name[i] + "  "+str(scores[i]))
#     i+=1


# scores = [10,87,9,25,89,33,77,99,82,4,7]

# max_number = scores[0]

# i = 0 

# while i < len(scores):
#     if scores [i] > max_number:
#         max_number = scores[i]
#     i += 1

# print(max_number)

# name = "nikax"

# scores = [10,25,35,12,33]

# i = 0

# while i < len(name):
#     print(name[i] + " " + str(scores[i]))

#     i += 1


# 3) students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]

# შეატრიალეთ უკუღმა sort და  revers-ის გარეშე




students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]

new_arr =[]

i = len(students)


while i > 0:
    new_arr.append(students[i-1])
    i -= 1
print(new_arr)