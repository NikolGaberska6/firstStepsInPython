one_year_taxes = int(input())

basketball_shoes = one_year_taxes - (one_year_taxes * 40/100)
basketball_team = basketball_shoes - (basketball_shoes * 20/100)
basketball_ball = 1/4 * basketball_team
basketball_accesories = 1/5 * basketball_ball

all_price = one_year_taxes + basketball_shoes + basketball_team + basketball_ball + basketball_accesories
print (all_price)