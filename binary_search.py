def inptr(lst):
    lst = list()
    inp = input('Введите что-нибудь: ')
    while inp != '': 
        lst.append(int(inp))
        inp = input('Введите что-нибудь: ')
    return lst


def bnr_srch(list, key):
    lwr_bnd = 0 
    ppr_bnd = len(list) - 1
    while lwr_bnd <= ppr_bnd:
        md = (lwr_bnd + ppr_bnd) // 2
        if list[md] == key:   
            for n in range(md + 1):
                if list[md] == list[n] and n < md:
                    md = n
            return md
        else:
            if key < list[md]:
                ppr_bnd = md - 1
            else:
                lwr_bnd = md + 1
    return None


x = inptr(lst=[])
x = sorted(x)
print(x)
print(bnr_srch(x, key=int(input("Введите искомый элемент: "))))


assert bnr_srch([], 42) is None
assert bnr_srch([0], 0) == 0
assert bnr_srch([0], 1) is None
assert bnr_srch([-1, 0, 42], 0) == 1
assert bnr_srch([-42, 0, 42], 42) == 2
assert bnr_srch([-6, -5, -4, -3, -2, -1], -4) == 2
assert bnr_srch([1, 2, 3, 4, 5, 6], 4) == 3
assert bnr_srch([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert bnr_srch([1, 2, 3, 4, 5], 7) is None
assert bnr_srch([1, 2, 3, 4, 5, 6], 7) is None
assert bnr_srch([42, 42, 42, 42, 42], 42) == 0
assert bnr_srch([-42, -42, -42, -42, -42], -42) == 0
assert bnr_srch([42, 42, 42, 42, 43], 43) == 4
assert bnr_srch([41, 42, 42, 42, 42], 41) == 0
assert bnr_srch([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert bnr_srch([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4