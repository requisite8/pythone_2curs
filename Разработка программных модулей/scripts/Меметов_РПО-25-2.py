"""
Элементы высшей математики, РПО-25/2.
Формула Муавра: [r(cos φ + i sin φ)]^n = r^n (cos nφ + i sin nφ),  n ∈ N.

=====================================================================
АНАЛИТИЧЕСКОЕ ДОКАЗАТЕЛЬСТВО (метод математической индукции)
=====================================================================
Обозначим z = r(cos φ + i sin φ) и P(n): z^n = r^n (cos nφ + i sin nφ).

1. База индукции (n = 1):
   z^1 = r(cos φ + i sin φ) = r^1 (cos(1·φ) + i sin(1·φ)).  P(1) верно.

2. Индукционное предположение (n = k):
   Пусть для некоторого k ∈ N верно z^k = r^k (cos kφ + i sin kφ).

3. Индукционный переход (n = k + 1):
   z^(k+1) = z^k · z = r^k (cos kφ + i sin kφ) · r (cos φ + i sin φ)
           = r^(k+1) · (cos kφ + i sin kφ)(cos φ + i sin φ).
   Раскрываем скобки:
     cos kφ cos φ + i cos kφ sin φ + i sin kφ cos φ + i² sin kφ sin φ.
   Так как i² = -1, группируем действительную и мнимую части:
     = (cos kφ cos φ - sin kφ sin φ) + i (sin kφ cos φ + cos kφ sin φ).
   По формулам сложения углов:
     cos(α + β) = cos α cos β - sin α sin β,
     sin(α + β) = sin α cos β + cos α sin β,
   где α = kφ, β = φ, получаем:
     = cos((k+1)φ) + i sin((k+1)φ).
   Значит z^(k+1) = r^(k+1) (cos((k+1)φ) + i sin((k+1)φ)), т.е. P(k+1) верно.

По принципу математической индукции P(n) верно для всех n ∈ N.  ∎

=====================================================================
ДОП. ЗАДАНИЕ: Ханойская башня, H(N) = 2^N - 1 — минимальное число ходов
=====================================================================
Чтобы переложить самый большой (N-й) диск, все N-1 меньших дисков должны
лежать на третьем стержне, а целевой стержень должен быть пуст. Поэтому
любое решение содержит: перенос N-1 дисков (≥ H(N-1) ходов), один ход
большого диска, ещё раз перенос N-1 дисков на него (≥ H(N-1) ходов).
Отсюда H(N) = 2·H(N-1) + 1, и рекурсивный алгоритм эту оценку достигает.

1. База (N = 1): один ход, 2^1 - 1 = 1.  Верно.
2. Предположение: H(k) = 2^k - 1.
3. Переход: H(k+1) = 2·H(k) + 1 = 2(2^k - 1) + 1 = 2^(k+1) - 1.  ∎
=====================================================================

Только стандартная библиотека: math и random — встроенные модули Python.
"""

import math
import random


# ---------------------------------------------------------------------
# Часть 1. Символьная проверка индукционного перехода.
#
# Многочлен храним как словарь {моном: коэффициент}.
#   моном       — отсортированный кортеж имён множителей, например
#                 ("cos(3φ)", "sin(φ)") означает cos(3φ)·sin(φ);
#   коэффициент — гауссово целое (re, im), т.е. re + i·im.
# Мнимую единицу i держим в коэффициенте, поэтому правило i² = -1
# срабатывает само собой при умножении коэффициентов.
# ---------------------------------------------------------------------

def gauss_mul(a, b):
    """(a0 + i·a1)(b0 + i·b1) = (a0·b0 - a1·b1) + i(a0·b1 + a1·b0)."""
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def poly_mul(p, q):
    """Раскрытие скобок: каждый член p умножается на каждый член q."""
    result = {}
    for mono_p, coef_p in p.items():
        for mono_q, coef_q in q.items():
            mono = tuple(sorted(mono_p + mono_q))
            coef = gauss_mul(coef_p, coef_q)
            old = result.get(mono, (0, 0))
            result[mono] = (old[0] + coef[0], old[1] + coef[1])
    # Убираем члены, которые взаимно уничтожились
    return {m: c for m, c in result.items() if c != (0, 0)}


def split_re_im(p):
    """Делит многочлен на действительную и мнимую части (обе — с целыми коэфф.)."""
    re_part = {m: c[0] for m, c in p.items() if c[0] != 0}
    im_part = {m: c[1] for m, c in p.items() if c[1] != 0}
    return re_part, im_part


def angle(n):
    """Имя угла nφ: 'φ' при n = 1, иначе '3φ' и т.п."""
    return "φ" if n == 1 else f"{n}φ"


def cis(n):
    """Символьное cos(nφ) + i·sin(nφ)."""
    return {
        (f"cos({angle(n)})",): (1, 0),
        (f"sin({angle(n)})",): (0, 1),
    }


def addition_formulas(k):
    """
    Формулы сложения углов для α = kφ, β = φ, записанные в том же виде,
    что и результат раскрытия скобок:
      cos((k+1)φ) = cos kφ cos φ - sin kφ sin φ
      sin((k+1)φ) = sin kφ cos φ + cos kφ sin φ
    """
    ck, sk = f"cos({angle(k)})", f"sin({angle(k)})"
    c1, s1 = "cos(φ)", "sin(φ)"
    cos_sum = collect([((ck, c1), 1), ((sk, s1), -1)])
    sin_sum = collect([((sk, c1), 1), ((ck, s1), 1)])
    return cos_sum, sin_sum


def collect(terms):
    """
    Собирает подобные члены. Нужно при k = 1: там sin φ·cos φ + cos φ·sin φ
    — это один и тот же моном, и он должен дать коэффициент 2.
    """
    result = {}
    for factors, coef in terms:
        mono = tuple(sorted(factors))
        result[mono] = result.get(mono, 0) + coef
    return {m: c for m, c in result.items() if c != 0}


def poly_to_str(p):
    """Человекочитаемый вид многочлена с целыми коэффициентами."""
    parts = []
    for mono, coef in sorted(p.items()):
        sign = "-" if coef < 0 else "+"
        value = "·".join(mono)
        if abs(coef) != 1:
            value = f"{abs(coef)}·{value}"
        parts.append(f"{sign} {value}")
    text = " ".join(parts)
    return text[2:] if text.startswith("+ ") else text


def prove_step_symbolic(k, verbose=True):
    """
    Индукционный переход k -> k+1 в символьном виде.
    Предполагаем z^k = r^k·cis(kφ) и показываем, что z^k · z = r^(k+1)·cis((k+1)φ).
    """
    # Модуль: r^k · r^1 = r^(k+1) — степени складываются
    r_power = k + 1

    # Аргумент: раскрываем (cos kφ + i sin kφ)(cos φ + i sin φ)
    product = poly_mul(cis(k), cis(1))
    re_part, im_part = split_re_im(product)

    cos_sum, sin_sum = addition_formulas(k)
    ok = re_part == cos_sum and im_part == sin_sum and r_power == k + 1

    if verbose:
        print(f"Шаг k = {k} -> k + 1 = {k + 1}")
        print(f"  модуль:  r^{k} · r = r^{r_power}")
        print(f"  Re: {poly_to_str(re_part)}  =  cos({angle(k + 1)})"
              f"  {'✓' if re_part == cos_sum else '✗'}")
        print(f"  Im: {poly_to_str(im_part)}  =  sin({angle(k + 1)})"
              f"  {'✓' if im_part == sin_sum else '✗'}")
    return ok


# ---------------------------------------------------------------------
# Часть 2. Численная проверка.
# Комплексное число храним как пару (a, b) = a + i·b, без типа complex,
# чтобы умножение было написано руками — тем же раскрытием скобок.
# ---------------------------------------------------------------------

def c_mul(z, w):
    """(a + ib)(c + id) = (ac - bd) + i(ad + bc)."""
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def moivre(r, phi, n):
    """Правая часть формулы: r^n (cos nφ + i sin nφ)."""
    return (r ** n * math.cos(n * phi), r ** n * math.sin(n * phi))


def close(z, w, rel_tol=1e-9):
    """Сравнение с допуском: float-арифметика не бывает абсолютно точной."""
    scale = max(1.0, abs(w[0]), abs(w[1]))
    return abs(z[0] - w[0]) <= rel_tol * scale and abs(z[1] - w[1]) <= rel_tol * scale


def check_induction_numeric(r, phi, n_max):
    """
    Идём по индукции: база z^1, затем каждый следующий z^(k+1) получаем
    как z^k · z и сверяем с формулой Муавра.
    """
    z = (r * math.cos(phi), r * math.sin(phi))

    # База индукции
    state = z
    if not close(state, moivre(r, phi, 1)):
        return False, 1

    # Переходы k -> k+1
    for k in range(1, n_max):
        state = c_mul(state, z)
        if not close(state, moivre(r, phi, k + 1)):
            return False, k + 1
    return True, n_max


# ---------------------------------------------------------------------
# Доп. задание: Ханойская башня
# ---------------------------------------------------------------------

def hanoi(n, source, target, spare, moves):
    """
    Перенести n дисков с source на target:
      1) n-1 дисков на запасной стержень,
      2) самый большой диск на целевой,
      3) n-1 дисков с запасного на целевой.
    """
    if n == 0:
        return
    hanoi(n - 1, source, spare, target, moves)
    moves.append((n, source, target))
    hanoi(n - 1, spare, target, source, moves)


def run_hanoi(n):
    moves = []
    hanoi(n, "A", "C", "B", moves)
    for step, (disk, src, dst) in enumerate(moves, start=1):
        print(f"  {step:>3}. диск {disk}: {src} -> {dst}")
    print(f"  Всего ходов: {len(moves)}, 2^{n} - 1 = {2 ** n - 1}"
          f"  {'✓' if len(moves) == 2 ** n - 1 else '✗'}")


# ---------------------------------------------------------------------

def main():
    print("=== Формула Муавра: символьная проверка ===")
    print("База n = 1: r^1·(cos φ + i sin φ) совпадает с z по определению ✓\n")
    k = int(input("Введите шаг k (натуральное число): "))
    if k < 1:
        print("k должно быть натуральным (k ≥ 1).")
        return
    print()
    if prove_step_symbolic(k):
        print(f"\nИз P({k}) следует P({k + 1}) — переход доказан.\n")
    else:
        print("\nПереход не сошёлся — где-то ошибка.\n")

    # Переход не зависит от конкретного k, но прогоним несколько подряд
    all_ok = all(prove_step_symbolic(j, verbose=False) for j in range(1, 51))
    print(f"Символьный переход для k = 1..50: {'✓' if all_ok else '✗'}\n")

    print("=== Формула Муавра: численная проверка ===")
    for _ in range(5):
        r = random.uniform(0.5, 1.5)
        phi = random.uniform(-math.pi, math.pi)
        ok, n = check_induction_numeric(r, phi, 30)
        status = "✓" if ok else f"✗ (расхождение на n = {n})"
        print(f"  r = {r:.4f}, φ = {phi:+.4f}, n = 1..30: {status}")

    print("\n=== Доп. задание: Ханойская башня ===")
    n = int(input("Введите число дисков N: "))
    run_hanoi(n)


if __name__ == "__main__":
    main()
