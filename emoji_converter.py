#This code uses a dictionary to translate symbols to emojis
def emoji_converter(message):
    words=message.split( " ")
    #the avove command creats a list from your input
    emoji ={
        ":)":"😊",
        ":(": "☹️"
    }
    #This portion of code iterates over the list and replaces the symbol that are keys in your dictionary(emoji)
    output = ""
    for word in words:
        output+= emoji.get(word, word) + " "
    return output
       

message= input(" >> " )

print (emoji_converter( message))
