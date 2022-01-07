# we want to create a dictionary of writer and their most famous quote

#objective : enter a writer, get a quote
#attention, the prgme should be able to pick up even if mispell

#source : name matching needs to be developped, can be a json file
#to import json file : loads("data.json") from there https://github.com/JamesFT/Database-Quotes-JSON/blob/master/quotes.json
import json
from difflib import get_close_matches

posts = json.load(open('quotes.json','r' , encoding='utf-8'))

var = input("Which author, would you like a quote from?   ").capitalize()

auth = []
for i in posts['quotes']:
    auth.append(i['author'])

aut = get_close_matches(var, auth)



def findquote(aut):
    quote = []
    noquote = []
    for i in posts['quotes']:
        if aut in i['author']:
            quote.append(i['quote'])
        else:
            noquote.append("...There's no official quote :-(...")
    if quote != []:
        return quote
    else:
        return noquote[0]


if aut != []:
    print(aut[0]+" said: ")
    output = findquote(aut[0])
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
else:
    print("No close match, try again")



