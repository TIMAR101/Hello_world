import collections

blocks = [4, 3, 2, 1, 3, 4]

dq = collections.deque(blocks)


def pile(dq):

    ground = float("inf")

    while dq:
        if dq[0] >= dq[-1]:
            block = dq.popleft()

        else:
            block = dq.pop()

        if block <= ground:
            ground = block

        else:
            return False

    return True

print(pile(dq))





