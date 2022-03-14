import matplotlib.pyplot as plt
def main():
    sales = [100,400,300,600]
    slise_labels = ['Quarter1','Quarter2','Quarter3','Quarter4']
    plt.pie(sales,labels=slise_labels)
    plt.title('Sale according to quarters.')
    plt.show()
main()