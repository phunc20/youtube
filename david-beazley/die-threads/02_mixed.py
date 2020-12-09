def you_say():
    print("Tomato")

async def i_say():
    print("Tomahto")

# Let's call the whole thing... "off"
async def spam():
    await i_say()
    you_say()
