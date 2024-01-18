class candidate():
    def __init__(self, firstName, surname, languages):
        self.firstName = firstName
        self.surname = surname
        self.languages = languages
        print(f'Hello, {self.firstName}!')    

candidate1 = candidate('Vivec', 'Ald', 'C')
candidate2 = candidate('Balmora', 'Sil', 'Python')
candidate3 = candidate('Branora', 'Port', 'C#')

def printDeets(n):
    print(n.firstName + ' ' + n.surname + ', ' + n.languages)

printDeets(candidate1)
printDeets(candidate2)
printDeets(candidate3)