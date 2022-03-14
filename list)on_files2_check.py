def main():
    cit = ['Szczecin', 'Wroclaw', 'Krakow', 'Warsw']
    file = open('cities.txt','w')
    for item in cit:
      file.write(item + '\n')
    file.close()
main()