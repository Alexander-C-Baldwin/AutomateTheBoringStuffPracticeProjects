#displays the inventory of a character from a dictionary parameter

from collections import Counter

def displayInv(inventory):
    print('Inventory:')

    itemTotal = 0

    for i , q in inventory.items():
        itemTotal += q
        print(q ,i)


    print('Total number of carried items: ' + str(itemTotal))

#add to inve function

def addToInv(inventory, addedItems):
    lootDic = {}
    newInv = inventory

    for i, c in Counter(addedItems).items():
        lootDic.setdefault(i,c)

    for i, v in lootDic.items():
        s = inventory.get(i, False)

        if s == False:
            newInv.setdefault(i, v)

        else:
            t = s + v
            newInv[i] = t

    return newInv



inv = {'gold coin': 16, 'rope': 2, 'mirror': 1, 'rapier': 1, 'mystic runes': 46, 'wand': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'Dragon Platebody', 'Dragon Scales']

print('Original Loot:\n')

displayInv(inv)

inv = addToInv(inv, dragonLoot)

print('\nAfter killing the Dragon:\n')

displayInv(inv)
