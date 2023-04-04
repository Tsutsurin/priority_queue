import heapq

add_element = lambda queue, _: heapq.heappush(queue, _)

rm_element = lambda queue: heapq.heappop(queue)

size = lambda queue: len(queue)

max = lambda queue: heapq.nlargest(1, queue)

def void(queue):
    _ = len(queue)
    if _ == 0:
        return 'Очередь пуста'
    else:
        return 'Очередь не пуста'
