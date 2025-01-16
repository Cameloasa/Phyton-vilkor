#scrimba
is_raining = False
is_cold = True
print("Good morning!")

if is_raining and is_cold: # or and
    print("Bring umbrella and jacket or both.")
elif is_raining and not (is_cold):
    print("Bring umbrella")
elif is_cold and not is_raining:
    print("Take your jacket!")
else:
    print("Umbrella optional.")

amount = 51


if amount <= 50:
    print("Purchase approved")
else:
    print("Please, enter your PIN: ")