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
    nnod = 21
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
    for nd in nodes:
        plt.text(nd.x, -0.02, f"{nd.index}", color="r")
    plt.plot([e.int_pts[0].x for e in elements],
             np.zeros(nnod-1), "xg", label="int_pts")
    for k, e in enumerate(elements):
        plt.text(e.int_pts[0].x, 0.02, f"{k}", color="g")
    plt.xlabel("x [m]")
    plt.legend()
    plt.title("Finite Element Mesh")
    plt.savefig("examples/heat_flow_mesh.png")

    # TODO: assign material properties and geometry to int pts
    # nodes[2]._x = 2.5
    print()
    for j, e in enumerate(elements):
        for ip in e.int_pts:
            ip.thrm_cond = thrm_cond
            ip.heat_trans_coef = heat_transfer_coef
            ip.area = A
            ip.perimeter = P
            ip.temp_inf = T_inf
        print(f"Element {j}")
        print(e.conduction_matrix)
        print(e.flux_vector)
        print()

    # TODO: build the global H matrix and Q vector
    Hg = np.zeros((nnod, nnod))
    Qg = np.zeros(nnod)
    for e in elements:
        # get element matrices and vectors
        He = e.conduction_matrix
        Qe = e.flux_vector
        # get global indices (dofs) for nodes in the element
        ind = [nd.index for nd in e.nodes]
        # stamp the element matrices/vectors into the global system
        Hg[np.ix_(ind, ind)] += He
        Qg[np.ix_(ind)] += Qe
    print("global system:")
    print(Hg)
    print(Qg)

    # TODO: assign boundary conditions
    Qg -= Hg[:, 0] * T_0
    Qg -= Hg[:, -1] * T_L

    # TODO: solve the global system
    Tg = np.zeros(nnod)
    Tg[1:-1] = np.linalg.solve(Hg[1:-1, 1:-1], Qg[1:-1])
    Tg[0] = T_0
    Tg[-1] = T_L
    for i, T in enumerate(Tg):
        nodes[i].temp = T
    print()
    print("temperature distribution:")
    print(Tg)

    # TODO: plot the temperature distribution
    plt.figure(figsize=(8.0, 3.0))
    plt.plot(x, Tg, "-r", label="temp dist")
    plt.plot([x[0], x[-1]], [T_inf, T_inf], "--k", label="ambient")
    plt.xlabel("x [m]")
    plt.ylabel("temp [deg C]")
    plt.savefig("examples/temp_distribution.png")


if __name__ == "__main__":
    main()
