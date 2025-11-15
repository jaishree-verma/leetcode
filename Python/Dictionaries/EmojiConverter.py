# Emoji Converter using dictionary
message = input(">")   # to take input from user
# it goes to string and find space then it uses as a boundary to seperate the string to multiple words and return lists
words = message.split(' ')
print(words)
emojis = {
    ":)": "😊",       # window : windows key + .
    "(:": "😔"       # mac : ctrl + cmd + space
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
