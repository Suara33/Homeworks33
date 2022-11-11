print ("this is second day")

name ="Tornike"

print(len(name))
#7

#my_sentence ="""გამარჯობა შეგახსენებთ რომ ყოველ დღე უნდა ისწავლოთ ახალი რამ პითონის შესახებ"""

#print(my_sentence)

knows_programming =True

if 10>5:
    print("hello")
#tab ის საშუალებით მოვახდინეთ ინდენტაცია (indentation)

if 25>5:
    print("you are the best")
full_name= "tornike suarishvili"
print(len(full_name))

#ყველა სტრინგი შეგვიძლია მივიჩნიოთ სიად
print(full_name[0])
#position = index  სინონიმებია

print("s" not in full_name)
print("t" in full_name)

full_name ="tornike suarishvili"
# print(full_name[2:9])
# print(full_name[2:9:2])
# #start:finish:step

# print(full_name[:5])
# print(full_name[5:13])
# print(full_name[5:])

print(full_name[-1])
print(full_name[-5])

print(full_name[-1:-6:-1])
# სტრინგებს აქვთ მეთოდები
#  1).სტრინგ.upper()
#  2).len.(სტრინგ)

print(full_name.upper())

name2 ="TORNIKE.suarishvili"
print(full_name.lower())

name3 ="     TORNIKE    "

print(name3.strip())

print(name2.replace("i","#"))

print(name2.replace("a","$"))