value = 7 / 3
# 1. Use the variable above to print this
# expected output:
#
# Value: 2.3333333333333335
# Two decimals: 2.33
# Percent, one decimal: 233.3%
print(f"{value}")
print(f"{value:.2f}")
print(f"{value:.1%}")



red = "red"
blue = "blue"
yellow = "yellow"
# 2. Use the three variables above to print this
# expected output:
#
# ----------------------------------
# |       red|      blue|    yellow|
# |red       |blue      |yellow    |
# |   red    |   blue   |  yellow  |
# ----------------------------------


print( "-" * 34)
print(f"|{red:>10}|{blue:>10}|{yellow:>10}|")
print(f"|{red:<10}|{blue:<10}|{yellow:<10}|")
print(f"|{red:^10}|{blue:^10}|{yellow:^10}|")
print( "-" * 34)
