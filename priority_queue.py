import heapq

def add_element(queue, _):
    heapq.heappush(queue, _)

def rem_element(queue):
    heapq.heappop(queue)

def void(queue):
    _ = len(queue)
    if _ == 0:
        return 'Очередь пуста'
    else:
        return 'Очередь не пуста'

def size(queue):
    _ = len(queue)
    return _