class ex5:
    name = 'Kevin J. El-Saikali'
    age = 17
    height = 90
    weight = 245
    eyes = 'black'
    teeth = 'white'
    hair = 'black'

    print(f"Let's talk about {name}.")
    print(f"He's {height} inches tall.")
    print(f"He's {weight}lbs heavy.")
    print("Boy is that heavy")
    print(f"He's got {eyes} eyes and {hair} hair.")
    print(f"His teeth are usually {teeth} depending on the coffee.")

    total = age + height + weight
    print(f"If I added my age: {age}, height: {height} and weight: {weight} together, I would get", total)

#This little f before the " (double-quote) and the 
# #{} characters tell Python 3, "Hey, this string needs to be formatted. Put these variables in there."