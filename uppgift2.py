#Balder
"""
2 Balder
För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!

Fråga användaren hur lång man är (i cm)
Skriv ut antingen "Du får åka!" eller "Du får inte åka"

Skriv in följande värden för att testa att ditt program gjort rätt:
121 cm (får inte åka)
130 cm (får åka)
155 cm (får åka)

Diskutera:
Varför just tre värden?
Varför dessa värden?
Skulle det vara bra att lägga till testvärdet 129 cm?

Ja, eftersom 129 cm är precis under gränsen och hjälper till att bekräfta att programmet inte felaktigt tillåter personer som är nära men under gränsen att åka.
Ett testvärde som 129 cm är särskilt användbart i fall där det kan finnas avrundningsproblem eller om det finns osäkerhet kring villkoret i koden.

Kom ihåg att göra code review!

"""

#Variant 1
user_input = input("Hur lång man är (i cm): ")
user_length = int(user_input)
allowed_length = 130


if user_length >= allowed_length:
    print("Du får åka!")
else:
    print("Du får inte åka!")


#Variant 2
length_test = [121, 129, 130, 155]
for length in length_test:
    if length >= 130:
        print(f"{length} cm: Du får åka!")
    else:
        print(f"{length} cm: Du får inte åka.")



