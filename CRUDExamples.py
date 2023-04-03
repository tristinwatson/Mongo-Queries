from AACoutcomes import AnimalShelter

#create animal
shelter = AnimalShelter()
data = {"age_upon_outcome": "1.7 years", "animal_type": "Cat"}

results = shelter.create(data)
print(results)

#read animal
shelter = AnimalShelter()
data = {"age_upon_outcome": "1.7 years", "animal_type": "Cat"}

results = shelter.read(data)
for x in results:
    print(x)

#create animal 2
shelter = AnimalShelter()
data = {"age_upon_outcome": "2.5 years", "animal_type": "Dog"}

results = shelter.create(data)
print(results)

#read animal 2
shelter = AnimalShelter()
data = {"age_upon_outcome": "2.5 years", "animal_type": "Dog"}

results = shelter.read(data)
for x in results:
    print(x)

#update animal 1
shelter = AnimalShelter()
data = {"age_upon_outcome": "1.7 years"}
newData = {"$set": {"age_upon_outcome": "3 years"}}

results = shelter.update(data, newData)
for x in results:
    print(x)

#delete animal 1
shelter = AnimalShelter()
data = {"age_upon_outcome": "5 years"}

results = shelter.delete(data)
for x in results:
    print(x)