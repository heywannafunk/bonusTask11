# 11. [10 баллов] Напишите программу, которая считывает из файла описание грамматики, удаляет из нее недостижимые
# символы и выводит текст с описанием новой грамматики. Грамматику описывать как в предыдущем задании.
import re

file = open("grammar2.txt", "r") 
grammarData = file.readline()
file.close()
#print(grammarData)

print()
print("исходная грамматика содержит следующие правила:")
grammarRules = grammarData.split(" ")
for rule in grammarRules:
    print(rule)

yi = [] #создаём множество достижимых символов
nonterminalSybmols = []
for rule in grammarRules:
    nonterminalSybmols.append(rule[0])
yi.append(set(nonterminalSybmols[0])) # записываем стартовый символ во множество достижимых
yi.append(set())

#print(nonterminalSybmols)
#print(yi)

i = 1
while not (yi[i-1] == yi[i-2]):
    for symbol in yi[i-1]:
        for rule in grammarRules:
            if rule.startswith(symbol):
                for char in rule:
                    if char != '-' and char != '>' and char != '|':
                        yi[i].add(char)
    yi.append(set())
    i=i+1

reachableSymbols = yi[-2]

#print(reachableSymbols)

newNonterminals = set(nonterminalSybmols).intersection(set(reachableSymbols)) #объединяем достижиме и нетерминалы - узнаём, какие нетерминалы достижимы
newGrammarRules = [] #создаём список новых правил
for symbol in newNonterminals:
    for rule in grammarRules:
        if rule.startswith(symbol):
            newGrammarRules.append(rule)

#print(newNonterminals)
#print(newGrammarRules)

print()
print("новая грамматика содержит следующие правила: ")
for rule in newGrammarRules:
    print(rule)





