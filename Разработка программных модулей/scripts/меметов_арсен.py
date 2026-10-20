from itertools import product

# Код каждой монеты: (взвешивание 1, взвешивание 2, взвешивание 3)
CODES = {
    1:  ( 1,  0,  0),
    2:  ( 1,  0, -1),
    3:  ( 1, -1,  1),
    4:  ( 1, -1, -1),
    5:  (-1,  1,  0),
    6:  (-1,  0, -1),
    7:  (-1, -1,  1),
    8:  (-1, -1,  0),
    9:  ( 0,  1,  1),
    10: ( 0,  1,  0),
    11: ( 0,  1, -1),
    12: ( 0,  0,  1),
}
N_WEIGHINGS = 3

# План взвешиваний строится из кодов: слева монеты с +1, справа с -1.
# Получается:
#   1) {1,2,3,4}   vs {5,6,7,8}
#   2) {5,9,10,11} vs {3,4,7,8}
#   3) {3,7,9,12}  vs {2,4,6,11}
PLAN = [
    (
        list(filter(lambda c: CODES[c][k] == 1, CODES)),   # левая чаша
        list(filter(lambda c: CODES[c][k] == -1, CODES)),  # правая чаша
    )
    for k in range(N_WEIGHINGS)
]

# Таблица расшифровки: вектор исходов -> (монета, характер дефекта).
# Это и есть всё «дерево решений», развёрнутое в словарь.
DECODE = {code: (coin, "тяжелее") for coin, code in CODES.items()}
DECODE.update({tuple(-x for x in code): (coin, "легче") for coin, code in CODES.items()})


def sign(x):
    """Знак числа без if: True/False в Python — это 1/0."""
    return (x > 0) - (x < 0)


def weigh(left, right, weights):
    """Одно взвешивание: +1 — левая тяжелее, -1 — правая, 0 — равновесие."""
    return sign(sum(weights[c] for c in left) - sum(weights[c] for c in right))


def make_weights(fake, heavier):
    """Все монеты весят 10, фальшивая — 11 или 9."""
    weights = dict.fromkeys(CODES, 10)
    weights[fake] = 10 + (2 * heavier - 1)  # heavier=True -> 11, False -> 9
    return weights


def find_fake(weights, verbose=False):
    """Делает ровно 3 взвешивания по плану и расшифровывает результат."""
    outcome = tuple(weigh(left, right, weights) for left, right in PLAN)
    verbose and print(f"  исходы взвешиваний: {outcome}")
    # .get на случай «невозможного» исхода (например, все монеты настоящие)
    return DECODE.get(outcome, (None, "исход невозможен при одной фальшивой монете"))


def self_check():
    """Проверяем все 24 варианта: какая монета фальшивая и в какую сторону."""
    assert all(len(l) == len(r) == 4 for l, r in PLAN), "на чашах должно быть по 4 монеты"
    assert len(DECODE) == 24, "все 24 ответа должны различаться"
    results = [
        find_fake(make_weights(coin, heavy)) == (coin, ("легче", "тяжелее")[heavy])
        for coin, heavy in product(CODES, (False, True))
    ]
    print(f"Проверено вариантов: {len(results)}, верно: {sum(results)}")
    assert all(results)


if __name__ == "__main__":
    print("План взвешиваний:")
    for i, (l, r) in enumerate(PLAN, 1):
        print(f"  {i}) {l} vs {r}")
    self_check()

    # Пример: 7-я монета легче
    print("\nПример: монета 7 легче")
    print("  ответ:", find_fake(make_weights(7, heavier=False), verbose=True))