#  import enum

from enum import Enum
import itertools

#make an enum for each continent pf risk 

class RiskContinent(Enum):
    NORTH_AMERICA = 1
    SOUTH_AMERICA = 2
    EUROPE = 3
    AFRICA = 4
    ASIA = 5
    AUSTRALIA = 6

# list the continent for risk 

continents = [RiskContinent.NORTH_AMERICA, RiskContinent.SOUTH_AMERICA, RiskContinent.EUROPE, RiskContinent.AFRICA, RiskContinent.ASIA, RiskContinent.AUSTRALIA]

# list link for each continent

links = {
    RiskContinent.NORTH_AMERICA: [RiskContinent.EUROPE, RiskContinent.ASIA, RiskContinent.SOUTH_AMERICA],
    RiskContinent.SOUTH_AMERICA: [RiskContinent.NORTH_AMERICA, RiskContinent.AFRICA],
    RiskContinent.EUROPE: [RiskContinent.NORTH_AMERICA, RiskContinent.AFRICA, RiskContinent.ASIA],
    RiskContinent.AFRICA: [RiskContinent.EUROPE, RiskContinent.SOUTH_AMERICA, RiskContinent.ASIA],
    RiskContinent.ASIA: [RiskContinent.NORTH_AMERICA, RiskContinent.EUROPE, RiskContinent.AFRICA, RiskContinent.AUSTRALIA],
    RiskContinent.AUSTRALIA: [RiskContinent.ASIA]
}


class Card:
  def __init__(self, continent, factoryPresence):
    self.continent = continent
    self.factoryPresence = factoryPresence

near = {}

for continent in continents:
    near[continent] = 0
    for link in links[continent]:
        near[continent] += len(links[link])

print("near")
print(near)

combs = []

for i in range(1, len(continents)+1):
    els = [list(x) for x in itertools.combinations(continents, i)]
    combs.extend(els)

#print(combs)
print(len(combs))

dict_cont = {
    "NA":RiskContinent.NORTH_AMERICA,
    "SA":RiskContinent.SOUTH_AMERICA,
    "EU":RiskContinent.EUROPE,
    "AF":RiskContinent.AFRICA,
    "AU":RiskContinent.AUSTRALIA,
    "AS":RiskContinent.ASIA
}

optimal_configurations = {
    3: {
        'Joueur 1': ['NA', 'SA', 'EU'],
        'Joueur 2': ['EU', 'AF', 'AS'],
        'Joueur 3': ['AS', 'AU', 'NA']
    },
    4: {
        'Joueur 1': ['NA', 'SA', 'EU'],
        'Joueur 2': ['EU', 'AF', 'AS'],
        'Joueur 3': ['AS', 'AU', 'NA'],
        'Joueur 4': ['AU', 'AF', 'SA']
    },
    5: {
        'Joueur 1': ['NA', 'SA', 'EU'],
        'Joueur 2': ['EU', 'AF', 'AS'],
        'Joueur 3': ['AS', 'AU', 'NA'],
        'Joueur 4': ['AU', 'AF', 'SA'],
        'Joueur 5': ['SA', 'NA', 'EU']
    },
    6: {
        'Joueur 1': ['NA', 'SA', 'EU'],
        'Joueur 2': ['EU', 'AF', 'AS'],
        'Joueur 3': ['AS', 'AU', 'NA'],
        'Joueur 4': ['AU', 'AF', 'SA'],
        'Joueur 5': ['SA', 'NA', 'EU'],
        'Joueur 6': ['EU', 'AS', 'AF']
    },
    7: {
        'Joueur 1': ['NA', 'SA', 'EU'],
        'Joueur 2': ['EU', 'AF', 'AS'],
        'Joueur 3': ['AS', 'AU', 'NA'],
        'Joueur 4': ['AU', 'AF', 'SA'],
        'Joueur 5': ['SA', 'NA', 'EU'],
        'Joueur 6': ['EU', 'AS', 'AF'],
        'Joueur 7': ['NA', 'SA', 'AU']
    }
}

optimal_configurations_with_factories = {
    3: {
        'Joueur 1': [('NA', 1), ('SA', 0), ('EU', 0)],
        'Joueur 2': [('EU', 1), ('AF', 0), ('AS', 0)],
        'Joueur 3': [('AS', 1), ('AU', 0), ('NA', 0)]
    },
    4: {
        'Joueur 1': [('NA', 1), ('SA', 0), ('EU', 0)],
        'Joueur 2': [('EU', 1), ('AF', 0), ('AS', 0)],
        'Joueur 3': [('AS', 1), ('AU', 0), ('NA', 0)],
        'Joueur 4': [('AU', 1), ('AF', 0), ('SA', 0)]
    },
    5: {
        'Joueur 1': [('NA', 1), ('SA', 0), ('EU', 0)],
        'Joueur 2': [('EU', 1), ('AF', 0), ('AS', 0)],
        'Joueur 3': [('AS', 1), ('AU', 0), ('NA', 0)],
        'Joueur 4': [('AU', 1), ('AF', 0), ('SA', 0)],
        'Joueur 5': [('SA', 1), ('NA', 0), ('EU', 0)]
    },
    6: {
        'Joueur 1': [('NA', 1), ('SA', 0), ('EU', 0)],
        'Joueur 2': [('EU', 1), ('AF', 0), ('AS', 0)],
        'Joueur 3': [('AS', 1), ('AU', 0), ('NA', 0)],
        'Joueur 4': [('AU', 1), ('AF', 0), ('SA', 0)],
        'Joueur 5': [('SA', 1), ('NA', 0), ('EU', 0)],
        'Joueur 6': [('AF', 1), ('AS', 0), ('EU', 0)]
    },
    7: {
        'Joueur 1': [('NA', 1), ('SA', 0), ('EU', 0)],
        'Joueur 2': [('EU', 1), ('AF', 0), ('AS', 0)],
        'Joueur 3': [('AS', 1), ('AU', 0), ('NA', 0)],
        'Joueur 4': [('AU', 1), ('AF', 0), ('SA', 0)],
        'Joueur 5': [('SA', 1), ('NA', 0), ('EU', 0)],
        'Joueur 6': [('AF', 1), ('AS', 0), ('EU', 0)],
        'Joueur 7': [('EU', 1), ('SA', 0), ('AU', 0)]
    }
}

optimal_configurations_with_factories = {
    3: {
        'Joueur 1': {'NA': (3, 1), 'SA': (1, 0), 'EU': (2, 0)},
        'Joueur 2': {'EU': (3, 1), 'AF': (2, 0), 'AS': (1, 0)},
        'Joueur 3': {'AS': (3, 1), 'AU': (1, 0), 'NA': (2, 0)}
    },
    4: {
        'Joueur 1': {'NA': (2, 1), 'SA': (1, 0), 'EU': (2, 0)},
        'Joueur 2': {'EU': (2, 1), 'AF': (1, 0), 'AS': (2, 0)},
        'Joueur 3': {'AS': (2, 1), 'AU': (1, 0), 'NA': (2, 0)},
        'Joueur 4': {'AU': (2, 1), 'AF': (1, 0), 'SA': (2, 0)}
    },
    5: {
        'Joueur 1': {'NA': (2, 1), 'SA': (1, 0), 'EU': (2, 0)},
        'Joueur 2': {'EU': (2, 1), 'AF': (1, 0), 'AS': (2, 0)},
        'Joueur 3': {'AS': (2, 1), 'AU': (1, 0), 'NA': (2, 0)},
        'Joueur 4': {'AU': (2, 1), 'AF': (1, 0), 'SA': (2, 0)},
        'Joueur 5': {'SA': (2, 1), 'NA': (1, 0), 'EU': (2, 0)}
    },
    6: {
        'Joueur 1': {'NA': (2, 1), 'SA': (1, 0), 'EU': (2, 0)},
        'Joueur 2': {'EU': (2, 1), 'AF': (1, 0), 'AS': (2, 0)},
        'Joueur 3': {'AS': (2, 1), 'AU': (1, 0), 'NA': (2, 0)},
        'Joueur 4': {'AU': (2, 1), 'AF': (1, 0), 'SA': (2, 0)},
        'Joueur 5': {'SA': (2, 1), 'NA': (1, 0), 'EU': (2, 0)},
        'Joueur 6': {'AF': (2, 1), 'AS': (1, 0), 'EU': (2, 0)}
    },
    7: {
        'Joueur 1': {'NA': (1, 1), 'SA': (1, 0), 'EU': (1, 0)},
        'Joueur 2': {'EU': (1, 1), 'AF': (1, 0), 'AS': (1, 0)},
        'Joueur 3': {'AS': (1, 1), 'AU': (1, 0), 'NA': (1, 0)},
        'Joueur 4': {'AU': (1, 1), 'AF': (1, 0), 'SA': (1, 0)},
        'Joueur 5': {'SA': (1, 1), 'NA': (1, 0), 'EU': (1, 0)},
        'Joueur 6': {'AF': (1, 1), 'AS': (1, 0), 'EU': (1, 0)},
        'Joueur 7': {'EU': (1, 1), 'SA': (1, 0), 'AU': (1, 0)}
    }
}

# Notez que "NA" signifie Amérique du Nord, "SA" Amérique du Sud, "EU" Europe, "AF" Afrique, "AS" Asie, et "AU" Australie.

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

# Pour 3 joueurs :
# Joueur 1 (NA, SA, EU) a accès à EU (Joueur 2) et SA (Neutre).
# Joueur 2 (EU, AF, AS) a accès à NA (Joueur 1) et AS (Joueur 3).
# Joueur 3 (AS, AU, AF) a accès à AF (Neutre) et EU (Joueur 2).
# Avis : Équilibré. Chaque joueur a accès à un autre joueur et à un territoire neutre.

# Pour 4 joueurs :
# Joueur 1 (NA, SA, EU) a accès à EU (Joueur 2) et SA (Joueur 4).
# Joueur 2 (EU, AF, AS) a accès à NA (Joueur 1) et AS (Joueur 3).
# Joueur 3 (AS, AU, AF) a accès à AF (Joueur 4) et EU (Joueur 2).
# Joueur 4 (AU, AF, SA) a accès à SA (Joueur 1) et AF (Joueur 3).
# Avis : Équilibré. Chaque joueur a deux voisins distincts.

# Pour 5 joueurs :
# Joueur 1 (NA, SA, EU) a accès à EU (Joueur 2) et SA (Joueur 5).
# Joueur 2 (EU, AF, AS) a accès à NA (Joueur 1) et AS (Joueur 3).
# Joueur 3 (AS, AU, AF) a accès à AF (Neutre) et EU (Joueur 2).
# Joueur 4 (AU, AF, SA) a accès à SA (Joueur 5) et AF (Neutre).
# Joueur 5 (SA, NA, EU) a accès à NA (Joueur 1) et EU (Neutre).
# Avis : Équilibré. Chaque joueur a accès à un ou deux autres joueurs et à un territoire neutre.

# Pour 6 joueurs :
# Joueur 1 (NA, SA, EU) a accès à EU (Joueur 2) et SA (Joueur 5).
# Joueur 2 (EU, AF, AS) a accès à NA (Joueur 1) et AS (Joueur 3).
# Joueur 3 (AS, AU, AF) a accès à AF (Joueur 6) et EU (Joueur 2).
# Joueur 4 (AU, AF, SA) a accès à SA (Joueur 5) et AF (Joueur 6).
# Joueur 5 (SA, NA, EU) a accès à NA (Joueur 1) et EU (Joueur 2).
# Joueur 6 (AF, AS, EU) a accès à AS (Joueur 3) et AF (Joueur 4).
# Avis : Équilibré. Chaque joueur a accès à deux autres joueurs et pas d'accès au territoire neutre, ce qui peut être intéressant.

# Pour 7 joueurs :
# Joueur 1 (NA, SA, EU) a accès à EU (Joueur 2, Joueur 7) et SA (Joueur 5).
# Joueur 2 (EU, AF, AS) a accès à NA (Joueur 1) et AS (Joueur 3).
# Joueur 3 (AS, AU, AF) a accès à AF (Joueur 6) et EU (Joueur 2, Joueur 7).
# Joueur 4 (AU, AF, SA) a accès à SA (Joueur 5) et AF (Joueur 6).
# Joueur 5 (SA, NA, EU) a accès à NA (Joueur 1) et EU (Joueur 2, Joueur 7).
# Joueur 6 (AF, AS, EU) a accès à AS (Joueur 3) et AF (Joueur 4).
# Joueur 7 (EU, SA, AU) a accès à SA (Joueur 5) et EU (Joueur 1, Joueur 2).
# Avis: Équilibré, mais les joueurs 2, 3, 5 et 7 ont des accès multiples à un même continent (EU), ce qui pourrait ajouter une dynamique intéressante ou déséquilibrée, selon la façon dont cela est géré dans le gameplay.

# Dans l'ensemble, ces configurations semblent assez équilibrées en termes de possibilités d'interaction entre les joueurs. Certains ajustements pourraient être nécessaires en fonction de votre vision du gameplay, mais en général, la structure semble solide.

