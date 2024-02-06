import numpy as np
import matplotlib.pyplot as plt

from goph420_examples.interpolation import (
    shape,
)


def main():
    x = np.linspace(-5.0, 5.0, 11)
    y = np.exp(x)

    #Interpolate 1 target point
    xd = x[3:5]
    yd = x[3:5]
    s = 0.4
    N = shape(s)
    x_i = N @ xd
    y_i = N @ yd

    plt.plot(x, y, 'ok', label='data')
    plt.plot(x_i, y_i, 'xr', label='shape')

    # plt.show()
    plt.savefig('examples/interpolation_plot.png')


if __name__ == "__main__":
    main()
