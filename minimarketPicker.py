
import random
minimarketsList = ['Alfamart', 'Indomaret', 'Seven Eleven', 'Circle K']

def pickMinimarket():
    print(minimarketsList[random.randint(0, len(minimarketsList)-1)])
    
def addMinimarket(name):
    minimarketsList.append(name)

def removeMinimarket(name):
    minimarketsList.remove(name)
    
def listMinimarket():
    for minimarket in minimarketsList:
        print(minimarket)

while True:
    print('''
          
        [1] - List Minimarket
        [2] - Add Minimarket
        [3] - Remove Minimarket
        [4] - Pick Minimarket
        [5] - Exit
        
        ''')
    selection = input('Please select an option: ')
    
    if selection == '1':
        print('')
        listMinimarket()
    elif selection == '2':
        inName = input('Type name of the restaurant that you want to add : ')
        addMinimarket(inName)
    elif selection == '3':
        inName = input('Type name of the restaurant that you want to remove : ')
        removeMinimarket(inName)
    elif selection == '4':
        pickMinimarket()
    elif selection == '5':
        break
    else:
        print('\nError: Pease select one of the options above !')
    