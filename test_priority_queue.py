import priority_queue
import heapq

queue = []
heapq.heapify(queue)

buffer = True
while(buffer == True):
    _ = input('1: Проверить пуста ли очередь\n'
              '2: Размер очереди\n'
              '3: Добавить элемент\n'
              '4: Удалить элемент\n'
              '5: Показать очередь\n'
              '6: Показать максимальный элемент\n'
              '7: Выйти\n')
    match _:
        case '1':
            print(priority_queue.void(queue))
        case '2':
            print(priority_queue.size(queue))
        case '3':
            priority_queue.add_element(queue, int(input('Какой элемент добавить? ')))
        case '4':
            priority_queue.rm_element(queue)
        case '5':
            print(queue)
        case '6':
            print(priority_queue.max(queue))
        case '7':
            buffer = False
    print()
