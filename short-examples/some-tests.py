
def printDictionary():
    #A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
    myDic =	{
        "brand": "Ford",
        "model": "Mustang",-
        "year": 1964
    }
    return myDic

def printSets():
    #A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
    mySet = {"apple", "banana", "cherry"}
    return mySet

def printTuple():
    #A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
    myTuple = ("apple", "banana", "tomato")
    return myTuple

def printList():
    #List is a collection which is ordered and changeable. Allows duplicate members.
    myList = ["apple", "banana", "tomato" ]
    return myList

def main():
    print('System is runninig')

    print('printing list ',  printList())

    print('printing tuple', printTuple())

    print('printing sets', printSets())

    print('printing dictionary', printDictionary())

    
if __name__ == "__main__":
    main()
