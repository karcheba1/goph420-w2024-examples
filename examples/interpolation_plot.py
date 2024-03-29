import numpy as np
import matplotlib.pyplot as plt

from goph420_examples.interpolation import (
    shape,
)


def main():
    x = np.linspace(-5.0, 5.0, 11)
    y = np.exp(x)
    xi = []
    yi = []
    s = np.linspace(0, 1, 5)
    for i, _ in enumerate(x[:-1]):
        xd = x[i:i+2]
        yd = y[i:i+2]
        for sj in s:
            N = shape(sj)
            x_i = N @ xd
            y_i = N @ yd
            xi.append(x_i)
            yi.append(y_i)

    plt.plot(x, y, 'ok', label='data')
    plt.plot(xi, yi, '--r', label='shape')
    plt.xlabel('x')
    plt.ylabel('y = exp(x)')
    plt.legend()

    # plt.show()
    plt.savefig('examples/interpolation_plot.png')


if __name__ == "__main__":
    main()
