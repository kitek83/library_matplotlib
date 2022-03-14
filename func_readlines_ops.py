def main():
    file = open('cities.txt','r')
    cities = file.readlines()
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    file.close()
    print(cities)

main()