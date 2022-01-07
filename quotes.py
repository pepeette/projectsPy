# we want to create a dictionary of writer and their most famous quote

#objective : enter a writer, get a quote
#attention, the prgme should be able to pick up even if mispell

#source : name matching needs to be developped, can be a json file
#to import json file : loads("data.json") from there https://github.com/JamesFT/Database-Quotes-JSON/blob/master/quotes.json
import json

posts = json.load(open('quotes.json','r' , encoding='utf-8'))

inp = input("Which author, would you like a quote from?   ")

def var(inp):
    inp.lower()
    inp.title()
    inp.capitalize()
    return inp

var = var(inp)
print(var+" said: ")

def findquote(var):
    quote = []
    noquote = []
    for i in posts['quotes']:
        if var in i['author']:
            quote.append(i['quote'])
        else:
            noquote.append("...There's no quote :-(...")
    if quote != []:
        print(quote)
    else:
        print(noquote[0])

output = findquote(var)

