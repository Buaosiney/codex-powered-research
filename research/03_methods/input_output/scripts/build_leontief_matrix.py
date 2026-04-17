from __future__ import annotations


def format_matrix(name: str, matrix: list[list[float]]) -> str:
    rows = []
    for row in matrix:
        rows.append("[" + ", ".join(f"{value:8.4f}" for value in row) + "]")
    return f"{name} =\n" + "\n".join(rows)


def format_vector(name: str, vector: list[float]) -> str:
    rows = [f"[{value:8.4f}]" for value in vector]
    return f"{name} =\n" + "\n".join(rows)


def subtract_from_identity(matrix: list[list[float]]) -> list[list[float]]:
    return [
        [1.0 - matrix[0][0], -matrix[0][1]],
        [-matrix[1][0], 1.0 - matrix[1][1]],
    ]


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    scale = 1.0 / determinant
    return [
        [d * scale, -b * scale],
        [-c * scale, a * scale],
    ]


def multiply_matrix_vector(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    ]


def main() -> None:
    a_matrix = [
        [0.20, 0.10],
        [0.30, 0.20],
    ]
    final_demand = [100.0, 50.0]

    identity_minus_a = subtract_from_identity(a_matrix)
    leontief_inverse = inverse_2x2(identity_minus_a)
    total_output = multiply_matrix_vector(leontief_inverse, final_demand)

    print("Leontief inverse minimal example\n")
    print(format_matrix("A", a_matrix))
    print()
    print(format_matrix("I - A", identity_minus_a))
    print()
    print(format_matrix("L = (I - A)^(-1)", leontief_inverse))
    print()
    print(format_vector("y", final_demand))
    print()
    print(format_vector("x = Ly", total_output))


if __name__ == "__main__":
    main()

