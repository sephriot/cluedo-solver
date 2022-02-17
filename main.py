KnowledgeBase = {}

# P - osoba
# I - przedmiot
# L - miejsce
# PL - gracz

MyCards = ['P1', 'P2', 'I1', 'I2', 'L8']
MyCardTag = ['PL1', 'PL1']

for card in MyCards:
    KnowledgeBase[card] = MyCardTag

print(KnowledgeBase)

Questions = [
    ['P1', 'I1', 'L1', 'PL1', 'PL2'],

    ['P3', 'I4', 'L7', 'PL2', 'PL3'],
    ['P1', 'I3', 'L1', 'PL4', 'PL3'],
    ['P1', 'I3', 'L7', 'PL3', 'PL4'],
    ['P1', 'I4', 'L7', 'PL2', 'PL4'],

    ['P1', 'I5', 'L6', 'PL3', 'PL4'],
    ['P1', 'I5', 'L6', 'PL2', 'PL4'],
    ['P1', 'I5', 'L6', 'PL3', 'PL4']
]

changes = 1
while changes > 0:
    changes = 0
    for question in Questions:
        questionCpy = question.copy()
        if KnowledgeBase.get(question[0]) is MyCardTag or KnowledgeBase.get(question[0]) is [question[-2], question[-1]]:
            questionCpy.remove(question[0])
        if KnowledgeBase.get(question[1]) is MyCardTag or KnowledgeBase.get(question[1]) is [question[-2], question[-1]]:
            questionCpy.remove(question[1])
        if KnowledgeBase.get(question[2]) is MyCardTag or KnowledgeBase.get(question[2]) is [question[-2], question[-1]]:
            questionCpy.remove(question[2])

        if len(questionCpy) == 3:
            KnowledgeBase[questionCpy[0]] = [question[-2], question[-1]]
            Questions.remove(question)
            changes += 1

        if len(questionCpy) == 4 and Questions.count(question) > 1:
            KnowledgeBase[questionCpy[0]] = [question[-2], question[-1]]
            KnowledgeBase[questionCpy[1]] = [question[-2], question[-1]]
            changes += 1
            for i in range(0, Questions.count(question)):
                Questions.remove(question)

        if len(questionCpy) == 5 and Questions.count(question) > 2:
            KnowledgeBase[questionCpy[0]] = [question[-2], question[-1]]
            KnowledgeBase[questionCpy[1]] = [question[-2], question[-1]]
            KnowledgeBase[questionCpy[2]] = [question[-2], question[-1]]
            changes += 1
            for i in range(0, Questions.count(question)):
                Questions.remove(question)

Locations = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9']
Items = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6']
People = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']

for item in KnowledgeBase:
    try:
        Locations.remove(item)
    except ValueError:
        pass
    try:
        Items.remove(item)
    except ValueError:
        pass
    try:
        People.remove(item)
    except ValueError:
        pass
print(KnowledgeBase)
print(Questions)
print(People, Items, Locations)
