def annie():
    name = "Annie: "
    yield name + "Anything you can do, I can do better.\n" \
                 "       I can do anything better than you."
    yield name + "Yes, I can!"
    yield name + "Yes, I can!"
    yield name + "Yes, I can. Yes, I can!"


def frank():
    name = "Frank: "
    yield name + "No, you can't."
    yield name + "No, you can't."
    yield name + "No, you can't."


queue = [annie(), frank()]
while queue:
    singer = queue.pop(0)
    try:
        print(singer.send(None))
        queue.append(singer)
    except StopIteration:
        pass
