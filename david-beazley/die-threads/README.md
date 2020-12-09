## Mix normal functions with asynchronous functions

```bash
(torch1.6.0-py3.8) ~/.../youtube/david-beazley/die-threads ❯❯❯ cat 01_mixed.py
def you_say():
    print("Tomato")

    async def i_say():
        print("Tomahto")

# Let's call the whole thing... "off"
def spam():
    you_say()
        await i_say()
(torch1.6.0-py3.8) ~/.../youtube/david-beazley/die-threads ❯❯❯ python 01_mixed.py
File "01_mixed.py", line 10
    await i_say()
        ^
SyntaxError: 'await' outside async function
(torch1.6.0-py3.8) ~/.../youtube/david-beazley/die-threads ❯❯❯ cat 02_mixed.py
def you_say():
    print("Tomato")

    async def i_say():
        print("Tomahto")

# Let's call the whole thing... "off"
async def spam():
    await i_say()
        you_say()
(torch1.6.0-py3.8) ~/.../youtube/david-beazley/die-threads ❯❯❯ python 02_mixed.py
(torch1.6.0-py3.8) ~/.../youtube/david-beazley/die-threads ❯❯❯
```

## English corner
- **envision** `v.tr.` _To conceive or see something within one's mind. To imagine_

