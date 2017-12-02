import json
from difflib import get_close_matches


def retrunDefinition(dictDefination,word):

    if word.lower() in dictDefination:
        arrDef = dictDefination[word.lower()]
        for objectDef in arrDef:
            print(objectDef)
    elif word.upper() in dictDefination:
        arrDef = dictDefination[word.upper()]
        for objectDef in arrDef:
            print(objectDef)
    elif word.title() in dictDefination:
        arrDef = dictDefination[word.title()]
        for objectDef in arrDef:
            print(objectDef)
    else:
        possibleWords = get_close_matches(word.lower(),dictDefination.keys(),n=1,cutoff = 0.8)
        if len(possibleWords) > 0:
            inputResponse = input("Think you meant " + possibleWords[0] + " if Yes press y or if No press n : ")
            if inputResponse.lower() == "y":
                arrDef = dictDefination[possibleWords[0].lower()]
                for objectDef in arrDef:
                    print(objectDef)
            elif inputResponse.lower() == "n":
                print("The Word doesn't exist, Please double check the word!")
            else:
                print("We did not undestand your query, Sorry!")
        else:
            print("The Word doesn't exist, Please double check the word!")

dictDefinitions = json.load(open("data.json"))
userWord = input("Enter Word : ")
retrunDefinition(dictDefinitions,userWord)
