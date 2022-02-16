#this file outputs the type advantages based on the input using the information from the API

def getWeakness(userInput):
    print("userInput: ", userInput)
    print(typeDict[userInput[0]])
    weakness = []
    stringWeakness = ""
    for user in userInput:
        weakness.append(typeDict[user])
    

    arrayWeakness = convert2D(weakness)
    # for i in range(len(convert2D(weakness))):
    #     stringWeakness += arrayWeakness[i]
    #     stringWeakness += " "
    # print(stringWeakness)
    return arrayWeakness

def getList(dict):
    list = [] 
    for key in dict.keys():
        list.append(key)
    return list

def convert2D(array2D):
    array1D = []
    for i in array2D:
        for j in i:
            if j not in array1D:
                array1D.append(j)
    return array1D

def converToArray(stringType):
    return stringType.spilt()

        
testVal = "hello"

normal = []
fire = ["Grass", "Ice", "Bug"]
water = ["Fire", "Ground", "Rock"]
electric= ["Water", "Flying"]
grass = ["Water", "Ground", "Rock"]
ice = ["Grass", "Flying", "Dragon"]
fighting = ["Normal", "Ice", "Rock"]
poison = ["Grass", "Bug"]
ground = ["Fire", "Electric", "Poison", "Rock"]
flying = ["Grass", "Fighting", "Bug"]
psychic = ["Fighting", "Poison"]
bug = ["Grass", "Poison"]
rock = ["Fire", "Ice", "Flying", "Bug"]
ghost = ["Ghost"]
dragon = ["Dragon"]


typeDict = {"normal": normal, "fire":fire, "water":water, "electric":electric, "grass":grass, "ice":ice, 
        "fighting":fighting, "poison":poison, "ground":ground, "flying":fighting, "psychic":psychic, 
        "bug":bug, "rock":rock, "ghost":ghost, "dragon":dragon}

typeList = getList(typeDict)
# userInput = ["Psychic", "Bug"]

# weakness = convert2D(getWeakness(userInput))

# print(weakness)


