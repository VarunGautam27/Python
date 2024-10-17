# phone=input("Phone: ")
# digits_mapping = {
#     "1": "one",
#     "2": "Two",
#     "3": "Three"
# }
# output= ""
# for ch in phone:
#     output +=digits_mapping.get(ch, "!") + " "
# print(output)


message = input(">")
word = message.split(' ')
emojis = {
    ":)":"😂",":(":"😒"
}
output = ""
for words in word:
    output+= emojis.get(words,words) + ' '
print(output)
