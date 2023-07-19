import numpy as np


def raidan_distance():
    t1 = float(input("Enter the first latitude coordinate: "))
    t2 = float(input("Enter the second londitude coordinate: "))
    g1 = float(input("Enter the first latitude coordinate: "))
    g2 = float(input("Enter the second londitude coordinate: "))
    c = 6371.01

    d = c * (
        np.arccos(
            ((np.sin(t1)) * (np.sin(t2)))
            + ((np.cos(t1)) * (np.cos(t2)) * (np.cos(g1 - g2)))
        )
    )

    print(f"The radian distance between these two points is: {d: .2f} kilometers")


raidan_distance()
