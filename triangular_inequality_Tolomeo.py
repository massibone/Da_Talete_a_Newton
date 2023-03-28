import matplotlib.pyplot as plt

a = 3
b = 4
c = 6

if a + b > c and a + c > b and b + c > a:
    plt.plot([0, b, c], [0, 0, a], 'b-')
    plt.plot([0, a, c], [0, 0, b], 'b-')
    plt.plot([0, a, b], [0, c, 0], 'b-')
    plt.fill_between([0, b, c], [0, 0, a], color='green', alpha=0.2) # type: ignore
    plt.axis('equal')
    plt.show()
else:
    print("La disuguaglianza triangolare non è verificata per a = {}, b = {}, c = {}.".format(a, b, c))
