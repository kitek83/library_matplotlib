#This program displays easy line graph.
import matplotlib.pyplot as plt
def main():
    x_cords = [0,1,2,3,4]
    y_cords = [0,3,6,1,8]
    plt.plot(x_cords, y_cords, marker='s')
    plt.title('Data graph')
    plt.xlabel('Year')
    plt.ylabel('Sale')
    plt.grid(True)
    #Customizing the axle markets to suit your needs.
    plt.xticks([0,1,2,3,4],
               ['2016', '2017','2018','2019','2020'])
    plt.yticks([0,1,2,3,4,5,6,7,8],
               ['0mln','1mln','2mln','3mln','4mln','5mln','6mln','7mln','8mln'])
    plt.show()





main()