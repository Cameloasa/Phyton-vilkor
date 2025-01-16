"""
3 Sportresultat
Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
Exempel på output:

Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!

Version 2: programmet ska tala om ifall det blev oavgjort.

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

"""

print("The match is over, let's calculate the result!")

try:
    # Prompt the user for scores
    goals_tottenham = int(input("How many goals did Tottenham score? "))
    goals_liverpool = int(input("How many goals did Liverpool score? "))

    # Determine the result and margin of victory
    if goals_tottenham > goals_liverpool:
        difference = goals_tottenham - goals_liverpool
        goal_word = "goal" if difference == 1 else "goals"
        print(f"Tottenham won by {difference} {goal_word}!")
    elif goals_liverpool > goals_tottenham:
        difference = goals_liverpool - goals_tottenham
        goal_word = "goal" if difference == 1 else "goals"
        print(f"Liverpool won by {difference} {goal_word}!")
    else:
        print("The match ended in a draw!")
except ValueError:
    print("Error: Invalid input. Please enter numeric values for the scores.")

"""
1. 2-2 draw
2. 2-1 T won
3. 1-3 L won
4. user input abc
"""