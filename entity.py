import json

prof_dict = json.load(open('professions.json'))

class Entity:

    def __init__(self, profession, start_hp):
        self.profession = profession
        self.start_hp = start_hp
    
    @staticmethod
    def from_dict(prof_dict):
        profession = prof_dict["profession"]
        start_hp = prof_dict["start_hp"]
        return Entity(profession, start_hp)

#entities = {}

#for entity_dict in d:
#    profession = d["profession"]

for profession in prof_dict["professions"]:
    print(profession['spells'])


spells_dict = json.load(open('spells.json'))


class Spells:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    @staticmethod
    def from_dict(spells_dict):
        name = spells_dict('name')
        damage = spells_dict('damage')
        return Spells( name, damage)

print(Spells)


for spells in spells_dict["spells"]:
    print(f"{spells['name']} {spells['damage']} damage")