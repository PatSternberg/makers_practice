personDict = {
    'name': 'Pat',
    'surname': 'Skip',
    'country': 'UK'
}

print(f'My name is ' + personDict['name'])

capitalCities = {
    'UK': 'London',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

capitalCities['France'] = 'Paris'
capitalCities['Spain'] = 'Madrid'
capitalCities.clear()

print(capitalCities)

trialDict = {
    1: 'Yes',
    2: 'No'
}

trialDict.setdefault(3)

print(trialDict[3])

trialDict.setdefault(3, 'Maybe')
                     
print(trialDict[3])