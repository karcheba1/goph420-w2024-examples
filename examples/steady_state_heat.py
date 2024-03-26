import numpy as np
import matplotlib.pyplot as plt

from goph420_examples.classes import (
    Node,
    Element,
)


def main():
    # define boundary conditions
    T_0 = 2.0
    T_L = 18.0
    T_inf = 35.0

    # define geometry
    L = 5.0                     # length of the pipe
    D = 0.5                     # diameter
    P = np.pi * D               # perimeter
    A = 0.25 * np.pi * D ** 2   # area

    # define material properties
    thrm_cond = 25.0            # W/K
    heat_transfer_coef = 2.0    # W/m^2/K

    # TODO: create Nodes and Elements that define the mesh
    nnod = 6
    x = np.linspace(0.0, L, nnod)
    nodes = tuple(Node(k, xk) for k, xk in enumerate(x))
    for nd in nodes:
        print(f"Node {nd.index} is at x = {nd.x}, id: {id(nd)}")
    elements = tuple(
        Element((nd0, nd1), order=1)
        for nd0, nd1 in zip(nodes[:-1], nodes[1:])
    )
    for k, e in enumerate(elements):
        print(
            f"Element {k} "
            + f"has nodes {e.nodes[0].index} "
            + f"and {e.nodes[1].index}, "
            + f"int_pt at x = {e.int_pts[0].x}"
        )

    # plot the mesh
    plt.figure(figsize=(8.0, 3.0))
    plt.plot([nd.x for nd in nodes], np.zeros(nnod), "or", label="nodes")
    plt.plot([e.int_pts[0].x for e in elements],
             np.zeros(nnod-1), "xg", label="int_pts")
    plt.xlabel("x [m]")
    plt.legend()
    plt.title("Finite Element Mesh")
    plt.savefig("examples/heat_flow_mesh.png")

    # TODO: assign material properties and geometry to int pts

    # TODO: build the global H matrix and Q vector

    # TODO: assign boundary conditions

    # TODO: solve the global system

    # TODO: plot the temperature distribution


if __name__ == "__main__":
    main()
