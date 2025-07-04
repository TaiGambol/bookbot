from operator import itemgetter


def wordcount(document):
    words = document.split()
    wordcount = len(words)
    return wordcount
    
def charactercount(document):
    document = document.lower()
    char_dict = {}
    for char in document:
        char_dict[char] = char_dict.get(char, 0) +1
    return char_dict

def sortCount(items):
    return items["count"]

def charcountreport(dictionary):
    dictsSorted = []
    dt = dictionary.items()
    tempDict = {}
    for k,v in dt:
        if k.isalpha():
            tempDict = {"char":k, "count":v}
            dictsSorted.append(tempDict)
    dictsSorted = sorted(dictsSorted, key=sortCount, reverse=True)
    return dictsSorted
    
