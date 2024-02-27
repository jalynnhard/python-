#F-strings 

pay = 600
heat = 50.25
rent = 300.6

print(f"weekly pay: {pay:2.f}")
print(f"heat: {heat:2.f}")
print(f"rent: {rent:2.f}")

print(f"combined bill: ${(heat + rent:.2f}")