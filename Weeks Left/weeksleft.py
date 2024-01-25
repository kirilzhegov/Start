# Small script ot calculate how many weeks you have left in 90 years of life

# We determine the person age first

age = input()


# We set the default 90 year old weeks

years = 90 - int(age)

# We determine how many weeks are left

weeks = years * 52

# We print the resulsts of the survey

print(f"You have {weeks} weeks left in your life!")