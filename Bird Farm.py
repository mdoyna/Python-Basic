import math

price_one_egg = int(input())
chickens_firstm = int(input())
chickens_secondm = int(input())
chickens_thirdm = int(input())

eggs_one = (30 / 3) * 2
one_month_eggs = chickens_firstm * eggs_one
second_month_eggs = (chickens_secondm + chickens_firstm) * eggs_one
third_month_eggs = (chickens_thirdm + chickens_secondm + chickens_firstm) * eggs_one
eggs = (one_month_eggs + second_month_eggs + third_month_eggs)

totalwaste = eggs * 0.04
totalprice = (eggs - totalwaste) * price_one_egg
totalpricelv = math.floor(totalprice / 100)
print(f"Profit: {totalpricelv} Lv.")

