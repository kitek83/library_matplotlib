def main():
    cit = ['Szczecin', 'Wroclaw', 'Krakow', 'Warsw']
    file = open('cities.txt','w')
    file.writelines(cit)
    file.close()

main()