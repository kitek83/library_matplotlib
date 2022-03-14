import matplotlib.pyplot as plt
def main():
    x_cords = [0,1,2,3,4,5,6]
    y_cords = [0,3,5,2,6,7,8]
    plt.plot(x_cords, y_cords)
    plt.title('Sample chart')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True)
    plt.show()

main()