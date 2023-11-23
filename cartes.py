import json
# (number of total cards, number of factories)
optimal_configurations_with_more_cards_and_factories = {
    3: {
        'Joueur 1': {'NA': (6, 3), 'SA': (3, 1), 'EU': (3, 1)},
        'Joueur 2': {'EU': (6, 3), 'AF': (3, 1), 'AS': (3, 1)},
        'Joueur 3': {'AS': (6, 3), 'AU': (3, 1), 'AF': (3, 1)},
        'Neutre':   {'AF': (3, 1), 'SA': (3, 1), 'AU': (3, 1)}
    },
    4: {
        'Joueur 1': {'NA': (6, 3), 'SA': (3, 1), 'EU': (3, 1)},
        'Joueur 2': {'EU': (6, 3), 'AF': (3, 1), 'AS': (3, 1)},
        'Joueur 3': {'AS': (6, 3), 'AU': (3, 1), 'AF': (3, 1)},
        'Joueur 4': {'AU': (6, 3), 'AF': (3, 1), 'SA': (3, 1)},
        'Neutre':   {'AF': (3, 1), 'SA': (3, 1), 'EU': (3, 1)}
    },
    5: {
        'Joueur 1': {'NA': (6, 3), 'SA': (3, 1), 'EU': (3, 1)},
        'Joueur 2': {'EU': (6, 3), 'AF': (3, 1), 'AS': (3, 1)},
        'Joueur 3': {'AS': (6, 3), 'AU': (3, 1), 'AF': (3, 1)},
        'Joueur 4': {'AU': (6, 3), 'AF': (3, 1), 'SA': (3, 1)},
        'Joueur 5': {'SA': (6, 3), 'NA': (3, 1), 'EU': (3, 1)},
        'Neutre':   {'AF': (3, 1), 'SA': (3, 1), 'EU': (3, 1)}
    },
    6: {
        'Joueur 1': {'NA': (6, 3), 'SA': (3, 1), 'EU': (3, 1)},
        'Joueur 2': {'EU': (6, 3), 'AF': (3, 1), 'AS': (3, 1)},
        'Joueur 3': {'AS': (6, 3), 'AU': (3, 1), 'AF': (3, 1)},
        'Joueur 4': {'AU': (6, 3), 'AF': (3, 1), 'SA': (3, 1)},
        'Joueur 5': {'SA': (6, 3), 'NA': (3, 1), 'EU': (3, 1)},
        'Joueur 6': {'AF': (6, 3), 'AS': (3, 1), 'EU': (3, 1)},
        'Neutre':   {'AF': (3, 1), 'SA': (3, 1), 'EU': (3, 1)}
    },
    7: {
        'Joueur 1': {'NA': (6, 3), 'SA': (3, 1), 'EU': (3, 1)},
        'Joueur 2': {'EU': (6, 3), 'AF': (3, 1), 'AS': (3, 1)},
        'Joueur 3': {'AS': (6, 3), 'AU': (3, 1), 'AF': (3, 1)},
        'Joueur 4': {'AU': (6, 3), 'AF': (3, 1), 'SA': (3, 1)},
        'Joueur 5': {'SA': (6, 3), 'NA': (3, 1), 'EU': (3, 1)},
        'Joueur 6': {'AF': (6, 3), 'AS': (3, 1), 'EU': (3, 1)},
        'Joueur 7': {'EU': (6, 3), 'SA': (3, 1), 'AU': (3, 1)},
        'Neutre':   {'AF': (3, 2), 'SA': (3, 1), 'EU': (3, 1)}
    }
}

# count the numbers of card without factories and with factories for each number of players:

result = {}
for key in optimal_configurations_with_more_cards_and_factories.keys():
    result[key] = {}
    for player in optimal_configurations_with_more_cards_and_factories[key].keys():
        result[key][player] = {}
        for card in optimal_configurations_with_more_cards_and_factories[key][player].keys():
            result[key][player][card] = {}
            result[key][player][card]['without factories'] = 0
            result[key][player][card]['with factories'] = 0
        for card in optimal_configurations_with_more_cards_and_factories[key][player].keys():
            result[key][player][card]['without factories'] += optimal_configurations_with_more_cards_and_factories[key][player][card][0]-optimal_configurations_with_more_cards_and_factories[key][player][card][1]
            result[key][player][card]['with factories'] += optimal_configurations_with_more_cards_and_factories[key][player][card][1]

#write result in a json file

with open('optimal_configurations_with_more_cards_and_factories.json', 'w') as outfile:
    json.dump(result, outfile)


# make sum of each card for number of players

result2 = {}

for key in result.keys():
    result2[key] = {}
    for player in result[key].keys():
        for card in result[key][player].keys():
            result2[key][card] = {}
            result2[key][card]['without factories'] = 0
            result2[key][card]['with factories'] = 0
    for player in result[key].keys():
        for card in result[key][player].keys():
            result2[key][card]['without factories'] += result[key][player][card]['without factories']
            result2[key][card]['with factories'] += result[key][player][card]['with factories']

print(result2)

#write result 2 in a json file as sum of each card for number of players

with open('sum_of_each_card_for_number_of_players.json', 'w') as outfile:
    json.dump(result2, outfile)


#write rule in french :

rules = ""


for key in result2.keys():
    rules += "Pour " + str(key) + " joueurs :\n"
    for joueur in result[key].keys():
        rules += "  - " + str(joueur) + " :\n"
        for card in result[key][joueur].keys():
            rules += "    - " + str(card) + " : " + str(result[key][joueur][card]['without factories']) + " cartes sans usine, " + str(result[key][joueur][card]['with factories']) + " cartes avec usine\n"
    
    rules += "  - Total :\n"
    for card in result2[key].keys():
        rules += "    - " + str(card) + " : " + str(result2[key][card]['without factories']) + " cartes sans usine, " + str(result2[key][card]['with factories']) + " cartes avec usine\n"
    rules += "\n"
    
#write rules in a txt file

with open('rules_cards.txt', 'w') as outfile:
    outfile.write(rules)