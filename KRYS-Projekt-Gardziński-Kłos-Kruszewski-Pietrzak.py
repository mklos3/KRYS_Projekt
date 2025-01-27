import random


def gf2_rank(matrix):
    """
    Funkcja oblicza rząd macierzy (nad GF(2))
    przy wykorzystaniu redukcji Gaussa-Jordana w GF(2).
    """
    # Kopiujemy macierz, aby nie modyfikować oryginału
    mat = [row[:] for row in matrix]
    rows = len(mat)
    cols = len(mat[0]) if rows > 0 else 0

    rank_val = 0
    pivot_col = 0

    for r in range(rows):
        if pivot_col >= cols:
            break

        # Szukamy wiersza z jedynką w pivot_col
        pivot_row = r
        while pivot_row < rows and mat[pivot_row][pivot_col] == 0:
            pivot_row += 1

        # Jeśli nie znaleziono wiersza z jedynką w tej kolumnie,
        # przechodzimy do następnej kolumny
        if pivot_row == rows:
            pivot_col += 1
            continue

        # Zamiana wiersza obecnego (r) z pivot_row
        mat[r], mat[pivot_row] = mat[pivot_row], mat[r]

        # Teraz mat[r][pivot_col] to pivot (1). Redukujemy pozostałe wiersze
        for rr in range(rows):
            if rr != r and mat[rr][pivot_col] == 1:
                # Dodajemy (modulo 2) wiersz r do rr, aby wyzerować pivot_col w rr
                for cc in range(cols):
                    mat[rr][cc] ^= mat[r][cc]

        rank_val += 1
        pivot_col += 1

    return rank_val


def add_matrices_gf2(A, B):
    """
    Dodaje dwie macierze A i B (elementy w GF(2)),
    zwraca nową macierz C = A + B (xor na każdym elemencie).
    Zakładamy, że A i B mają takie same wymiary.
    """
    rows = len(A)
    cols = len(A[0])
    C = []
    for r in range(rows):
        row = [(A[r][c] ^ B[r][c]) for c in range(cols)]
        C.append(row)
    return C


def scalar_mult_matrix_gf2(scalar, A):
    """
    Mnoży macierz A przez skalar w GF(2).
    Skoro scalar jest 0 lub 1, to:
    - 0 * A = macierz zerowa,
    - 1 * A = A.
    """
    if scalar == 0:
        # Zwracamy macierz zerową o tych samych wymiarach
        rows = len(A)
        cols = len(A[0])
        return [[0] * cols for _ in range(rows)]
    else:
        # Zwracamy kopię A (bo 1 * A = A w GF(2))
        return [row[:] for row in A]


def linear_combination_gf2(matrices, coeffs):
    """
    Oblicza liniową kombinację macierzy (over GF(2))
    z wykorzystaniem współczynników w coeffs (również w GF(2)).

    matrices: lista macierzy [M1, M2, ..., Mk]
    coeffs: współczynniki [a1, a2, ..., ak] (0 lub 1)
    """
    # Zakładamy, że matrices i coeffs mają zgodne wymiary
    rows = len(matrices[0])
    cols = len(matrices[0][0])

    # Inicjujemy macierz wynikową jako macierz zerową
    result = [[0] * cols for _ in range(rows)]

    for M, a in zip(matrices, coeffs):
        # Dodajemy a*M do result
        mult = scalar_mult_matrix_gf2(a, M)
        result = add_matrices_gf2(result, mult)
    return result


def generate_random_matrix_gf2(n, m):
    """
    Generuje losową macierz n x m nad GF(2).
    """
    return [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]


def brute_force_min_rank(matrices, max_rank=1):
    """
    Naiwny atak typu MinRank (brute force) w GF(2),
    z pominięciem trywialnego rozwiązania (wszystkie współczynniki == 0).

    matrices: lista macierzy (każda o wymiarach n x m)
    max_rank: szukana maksymalna ranga (np. 1, 2, ...)
    """
    k = len(matrices)
    if k == 0:
        return None

    total_combinations = 1 << k  # 2^k

    # Rozpoczynamy od 1, żeby pominąć combo == 0 (czyli [0,0,...,0])
    for combo in range(1, total_combinations):
        # Budujemy wektor współczynników w GF(2)
        coeffs = [(combo >> i) & 1 for i in range(k)]

        # Obliczamy kombinację liniową
        comb_matrix = linear_combination_gf2(matrices, coeffs)

        # Sprawdzamy rangę
        rank_c = gf2_rank(comb_matrix)

        if rank_c <= max_rank:
            return coeffs, comb_matrix

    return None


def example_usage():
    # Przykład działania: mamy np. 3 macierze 4x4
    k = 5
    n = 6
    m = 6
    r = 3
    matrices = [generate_random_matrix_gf2(n, m) for _ in range(k)]

    # Wyświetlamy wygenerowane macierze
    print("Wygenerowane macierze (nad GF(2)):")
    for i, M in enumerate(matrices):
        print(f"M{i + 1}:")
        for row in M:
            print(row)
        print()

    # Próbujemy znaleźć kombinację liniową o rzędzie <= r
    result = brute_force_min_rank(matrices, max_rank=r)
    if result is not None:
        coeffs, comb_matrix = result
        print("Znaleziono współczynniki dające rząd <= "+str(r))
        print("Współczynniki:", coeffs,"\n")
        print("Kombinacja liniowa (macierz wynikowa):")
        for row in comb_matrix:
            print(row)
        print(f"Rząd = {gf2_rank(comb_matrix)}")
    else:
        print("Nie znaleziono żadnej kombinacji o rzędzie <= "+str(r))


if __name__ == "__main__":
    example_usage()
