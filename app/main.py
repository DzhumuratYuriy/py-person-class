
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    name_map = {p.name: p for p in person_list}
    for person in people:
        obj = name_map[person["name"]]
        wife = person.get("wife")
        husband = person.get("husband")
        if wife is not None and name_map[wife] is not None:
            obj.wife = name_map[wife]
        elif husband is not None and name_map[husband] is not None:
            obj.husband = name_map[husband]
        else:
            continue
    return person_list
