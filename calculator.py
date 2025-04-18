import random
import time
import sys
import pycountry

quotes = [
    "Trust me, it's the best tariff. Everybody says so!!!",
    "We're winning on trade. It's so beautiful!!!",
    "Nobody knows tariffs better than me. Nobody!!!",
    "I know tariffs. I invented tariffs!!!",
    "Elon told me this is how you win at trade. He's a very smart guy!",
    "Elon Musk said it’s the future of trade. I agree. 100%."
]

chinaquotes = [
    "Nobody’s tougher on China than me. Believe me!!!",
    "We're hitting China with tariffs they’ve never seen before!!!",
    "China thought they could play games. Not on my watch!!!",
    "This is how we win. Big tariffs. China pays!!!",
    "I told them: no more cheating, China!!!",
    "Even Elon said China needs to be handled. So I did.",
    "Elon called me and said, Your China tariffs? Genius!",
    "Me and Elon discussed this. He said, Put tariffs on China. Big ones!"
]

fakequotes = [
    "We tariff first. Ask questions later. That’s leadership!",
    "No idea where that is. But we're winning big with tariffs!",
    "Sounds made up. But just in case... TARIFFS!",
    "Never heard of it. Sounds suspicious. Tariffs applied.",
    "Is that even real? Doesn't matter — we hit it with tariffs!",
    "If it exists or not, who cares. We're putting tariffs on it!"
]

country = input("Enter a Country (EN)\n")
tariff = (random.randrange(20, 100))

def countrycheck(name):
    try:
        pycountry.countries.lookup(name)
        return True
    except LookupError:
        return False

if country.lower() == "china":
    tariff += 300

print("Calculating Tariffs:")
for i in range(0, 101, 5):
    bar = "█" * (i // 5)
    spaces = " " * ((100 - i) // 5)
    sys.stdout.write(f"\r[{bar}{spaces}] {i}%")
    sys.stdout.flush()
    time.sleep(0.1)

print(f"\n\nTariffs for {country}: {tariff}% — Great!\n")


if country.lower() == "china":
    print(random.choice(chinaquotes))
elif not countrycheck(country): 
    print(random.choice(fakequotes))
else: 
    print(random.choice(quotes))

input("\n\nPress ENTER to exit.")
