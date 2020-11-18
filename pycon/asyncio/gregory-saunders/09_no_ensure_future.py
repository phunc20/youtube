import asyncio

async def annie():
    name = "Annie: "
    print(name + "Anything you can do, I can do better.")
    print(' '*len(name) + "I can do anything better than you.")
    await frank()
    print(name + "Yes, I can!")
    await frank()
    print(name + "Yes, I can!")
    await frank()
    print(name + "Yes, I can. Yes, I certainly can!")


async def frank():
    name = "Frank: "
    print(name + "No, you can't.")


loop = asyncio.get_event_loop()
#future = loop.create_future()
#annie(future)
#frank(future)
#loop.run_until_complete(future)
#loop.run_until_complete(asyncio.ensure_future(annie()))
loop.run_until_complete(annie())
