d = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}


def print_all():
    for item in d:
        print(f"{item}==>{d[item]}")


def add():
    country = input("country name to add: ")
    if country in d:
        print("it already exist")
    else:
        population = input("population: ")
        d[country] = population
        for item in d:
            print(f"{item}==>{d[item]}")


def remove():
    country = input("country to remove: ")
    if country in d:
        del d[country]
        for item in d:
            print(f"{item}==>{d[item]}")
    else:
        print("that country doesn't exist!")


def query():
    country = input("country to query: ")
    print(f"{d[country]}")


while True:
    op = input("Choose the option- a:print, b: add, c:remove, d:query, e:exit:")
    match op:
        case "print":
            print_all()
        case "add":
            add()
        case "remove":
            remove()
        case "query":
            query()
        case "exit":
            break
