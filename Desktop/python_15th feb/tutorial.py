hours_in_a_day=24
days_in_a_year=365
minutes=60
seconds_in_minute=60
years=10

hours_in_year= hours_in_a_day*days_in_a_year
print(f"There are {hours_in_year}")

minutes_in_decade=60*10*hours_in_year
print (f"There are {minutes_in_decade}")

age_years=30
seconds_old= age_years*days_in_a_year*3600
print(f"I am {seconds_old} seconds old")

seconds_provided= 1406000000
age_from_seconds= seconds_provided / (days_in_a_year*hours_in_a_day*minutes*seconds_in_minute)
print(f"You are {age_from_seconds} years old")

for i in range(7,0,-1):
    for j in range(i):
        print("*",end="")
    print()

def triangle_area(b,h):
    return 0.5 * b * h

b=2.28
h=3.55

area=triangle_area(b,h)
print(f"Triangle area is {area}")