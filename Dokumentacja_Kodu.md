### Dokumentacja kodu

#### Opis funkcjonalności kodu
Główne funkcjonalności kodu obejmują:
- Obliczanie rzędu macierzy nad ciałem GF(2) z użyciem algorytmu Gaussa-Jordana (`gf2_rank`).
- Tworzenie losowych macierzy nad GF(2) (`generate_random_matrix_gf2`).
- Dodawanie i mnożenie macierzy przez skalary nad GF(2) (`add_matrices_gf2`, `scalar_mult_matrix_gf2`).
- Obliczanie kombinacji liniowych macierzy nad GF(2) (`linear_combination_gf2`).
- Przeprowadzanie ataku typu MinRank przy użyciu metody brute force (`brute_force_min_rank`).

#### Parametryzacja kodu
Parametry kodu mogą być zmieniane w funkcji `example_usage`, która ilustruje sposób użycia głównych funkcji:
- `k` - liczba macierzy wejściowych.
- `n`, `m` - liczba wierszy i kolumn macierzy.
- `r` - maksymalny rząd, dla którego kod szuka kombinacji liniowych macierzy (`max_rank`).

Zmiana tych parametrów pozwala użytkownikowi kontrolować wielkość danych wejściowych oraz granicę poszukiwań rzędu w ataku MinRank.

#### Wynik działania kodu
Wynikiem działania kodu jest:
- Lista współczynników kombinacji liniowej, które prowadzą do macierzy o rzędzie mniejszym bądź równym `max_rank`.
- Wynikowa macierz będąca kombinacją liniową z obliczonym rzędem.

#### Wyniki
- Jeśli atak się powiedzie, zostaną wypisane współczynniki kombinacji liniowej oraz wynikowa macierz.
- Jeśli atak się nie powiedzie, program poinformuje, że nie znaleziono żadnej kombinacji spełniającej warunek rzędu.
