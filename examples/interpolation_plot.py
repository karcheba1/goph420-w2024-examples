import numpy as np
import matplotlib.pyplot as plt

from goph420_examples.interpolation import (
    shape,
)


def main():
    x = np.linspace(-5.0, 5.0, 11)
    y = np.exp(x)

    plt.plot(x, y, 'ok', label='data')

    # plt.show()
    plt.savefig('examples/interpolation_plot.png')


if __name__ == "__main__":
    main()
