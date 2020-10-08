import asyncio

def annie(when_frank_is_done_future):
    name = "Annie: "
    print(name + "Anything you can do, I can do better.")
    print(' '*len(name) + "I can do anything better than you.")
    def defiance(_):
        print(name + "Yes, I can!")
    when_frank_is_done_future.add_done_callback(defiance)


def frank(when_frank_is_done_future):
    name = "Frank: "
    print(name + "No, you can't.")
    when_frank_is_done_future.set_result(None)


loop = asyncio.get_event_loop()
future = loop.create_future()
annie(future)
frank(future)
loop.run_until_complete(future)
