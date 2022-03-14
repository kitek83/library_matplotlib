import matplotlib.pyplot as plt
def main():
    x_cords = [0,1,2,3,4,5,6]
    y_cords = [0,3,4,5,3,8,9]
    plt.plot(x_cords,y_cords)
    plt.title('Thi is graph nr3')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.xlim(-1,15)
    plt.ylim(-1,20)
    plt.grid(True)
    plt.show()

main()