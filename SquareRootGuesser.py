import random
import numpy
from matplotlib import pyplot as plt


def root_guess(number):
    # Variables
    ceiling = 10000
    error = number
    root = 0.1
    steps = 0
    random.seed(version=2)
    guesses = []
    guesses_a = []

    # Guessing the roots until error is smaller then the precision required
    while abs(error) > 0.000000000000001:
        steps += 1
        if error > 0:
            root = (random.randint(0, ceiling)/ceiling * error) + root
        elif error < 0:
            root = (random.randint(0, ceiling)/ceiling * abs(error)) + (root + error)
        rest = number - (root * root)
        error = rest/root
        print('Root: %.25f' % root)
        print('Error: %.25f' % error)
        guesses.append(root)

    # Drawing the guesses and the final root found
    print("Number of guesses: %d" % steps)
    x = numpy.arange(0, steps, 1)
    for i in range(steps):
        guesses_a.append(root + abs(guesses[i] - root))
    gss2, = plt.plot(x, guesses_a, c="y")
    gss = plt.scatter(x, guesses, c="b", s=10)
    y = plt.axhline(y=root, c="r", lw=0.75, ls="--")
    plt.title('Root Guesses')
    plt.legend([y, gss2, gss], ['Found Root = %.5f' % root, '"Absolute" Guesses', 'Guesses (%d)' % steps])
    # plt.show()
    return root


# Calculating Phi based on the root guessing, just for fun :)
phi = (1 + root_guess(5))/2
print("Phi = %.25f" % phi)

# Showing results
plt.show()
