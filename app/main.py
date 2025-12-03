
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
        wife_name = person.get("wife")
        if wife_name is not None:
            spouse = name_map.get(wife_name)
            if spouse is not None:
                obj = name_map[person["name"]]
                obj.wife = spouse
            else:
                continue
    for person in people:
        husband_name = person.get("husband")
        if husband_name is not None:
            spouse = name_map.get(husband_name)
            if spouse is not None:
                obj = name_map[person["name"]]
                obj.husband = spouse
            else:
                continue
    return person_list
