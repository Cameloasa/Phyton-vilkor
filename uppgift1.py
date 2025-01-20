is_member = False
level1 = 100
level2 = 300
discount = 0

while True:
    try:
        price = float(input("Välkommen, köp något dyrt: "))
        if price <= 0:
            print("Priset måste vara större än 0! Försök igen.")
        else:
            break
    except ValueError:
        print("Felaktig input! Vänligen ange ett giltigt nummer.Använd siffror och punkt (.) för decimaler.")

if price < level1 and is_member:
    print(f"Du får inget rabat, du måste spendera minst {level1}kr för att kunna få rabatt.")
elif level2 > price >= level1 and not is_member:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = 10
elif price >= level2 and not is_member:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = 25
elif price == level1:
    print("Grattis! Du har nått nivå 1 och får 10% rabatt.")
    discount = 10
elif price == level2:
    print("Grattis! Du har nått nivå 2 och får 25% rabatt.")
    discount = 25

final_price = price * (100 - discount) / 100
print(f"Efter rabatter blir priset: {final_price:.2f} kr")

print("**********************")

"""
Tester:

Input: -10
Output: "Priset måste vara ett positivt nummer större än 0. Försök igen."
Input: abc
Output: "Felaktig input! Vänligen ange ett giltigt nummer.Använd siffror och punkt (.) för decimaler."
Input: 50
Output: "Du får inget rabat, du måste spendera minst 100kr för att kunna få rabatt."
Input: 100
Output: "Grattis! Du har nått nivå 1 och får 10% rabatt."
Input: 150
Output: "Grattis! Du har avancerat till nivå 1 och får 10% rabatt."
Input: 300
Output: "Grattis! Du har nått nivå 2 och får 25% rabatt."
Input: 400
Output: "Grattis! Du har avancerat till nivå 2 och får 25% rabatt."
Input: 123,45
Output: Felaktig input! Vänligen ange ett giltigt nummer.Använd siffror och punkt (.) för decimaler.
"""

"""
#Verison 2
is_member = False
level1 = 100
level2 = 300
discount = 0

try:
    price = float(input("Välkommen, köp något dyrt: "))

    if price <= 0:
        print("Priset måste vara större än 0! Försök igen.")
    else:
        if level1 < price < level2:
            print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
            discount = 10
        elif price >= level2:
            print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
            discount = 25

        final_price = price * (100 - discount) / 100
        print(f"Efter rabatter blir priset: {final_price:.2f} kr")
except ValueError:
    print("Endast siffror är giltigt att mata in!")
"""