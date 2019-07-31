# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

num5 = 5
num6 = 6

bin_num5 = (f'five in binary: {bin(num5)}')   # 0b 0101, note that python cut left zeros and show us 0b 101
bin_num6 = (f'six in binary: {bin(num6)}')   # 0b 0110
print(bin_num5, bin_num6, sep='\n')

# bls - bitwise left shift. Example: foo << 3 will do it three times
bls_num5 = num5 << 2    # 0101-before shift, 1010-first shift, second shift = 0b 10100 = 20
brs_num5 = num5 >> 2    # 0010-first shift, second shift = 0001 = 1

print(f'Result of double bitwise left shift: {bls_num5}')
print(f'Result of double bitwise right shift: {brs_num5}')


lor = 5 | 6         # logical 'OR'
land = 5 & 6        # logical 'AND'
lnot5 = ~5           # logical 'NOT' of 5
lnot6 = ~6           # logical 'NOT' of 6
lxor = 5 ^ 6        # logical 'XOR'

print(f'Result of lor: {lor}')
print(f'Result of land: {land}')
print(f'Result of lnot5: {lnot5}')
print(f'Result of lnot6: {lnot6}')
print(f'Result of lxor: {lxor}')
