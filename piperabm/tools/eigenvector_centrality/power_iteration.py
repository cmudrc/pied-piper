import numpy as np

# Define the matrix A
arr = [
    [0.49, 0.49, 0.02],
    [0.49, 0.49, 0.02],
    [0.02, 0.02, 0.96]
]

arr = [
    [0.4, 0.3, 0.3],
    [0.25, 0.5, 0.25],
    [0.6, 0, 0.4]
]

def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break

        v = v_new
        ev = ev_new

    return ev_new, v_new

ev_new, v_new = power_iteration(np.array(arr))
print(v_new)
