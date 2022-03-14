import matplotlib.pyplot as plt
def main():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]

    plt.grid(True)
    plt.xticks([5,15,25,35,45],
               ['2015','2016','2017','2018','2019'])
    plt.yticks([0,100,200,300,400,500],
               ['0mln','1mln','2mln','3mln','4mln','5mln'])
    bar_width = 10
    plt.bar(left_edges, heights,bar_width,color=('b','g','r','y','c'))
    plt.xlabel('Year')
    plt.ylabel('Sale')
    plt.title('Sale during the years.')
    plt.show()


main()