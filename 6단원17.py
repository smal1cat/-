# 연결 리스트.
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

# 연결 큐.
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):                     # 큐가 비어있는지 여부를 확인하는 메소드
        return self.front is None

    def enqueue(self, elem):            # 큐에 원소를 추가하는 메소드
        new_node = Node(elem)
        if self.isEmpty():                  # 큐가 비었을 경우  
            self.front = new_node      # front와 rear가 새로운 노드를 가리키도록 설정한다
            self.rear = new_node
        else:                                # 큐가 비어있지 않을 경우 
            self.rear.link = new_node  #현재 rear의 다음 노드로 새로운 노드를 연결 후 갱신한다
            self.rear = new_node

    def dequeue(self):                       # 큐에서 원소를 제거하고 반환하는 메소드
        if self.isEmpty():
            return None                 
        else:                                   # front가 가리키는 노드의 데이터를 저장하고
            front_data = self.front.data   # front를 다음 노드로 갱신
            self.front = self.front.link
            return front_data

    def __str__(self):                        # 큐의 상태를 문자열로 표현하는 메소드
        arr = []
        node = self.front
        while node is not None:          # 큐의 각 노드의 데이터를 리스트에 추가
            arr.append(node.data)
            node = node.link
        return str(arr)


queue = LinkedQueue()

for i in range(1, 10):                       # 큐에 1부터 9까지의 원소를 추가
    queue.enqueue(i)

print("큐에 1부터 9까지의 원소를 추가한 후의 큐 상태:", queue)


while not queue.isEmpty():                # 큐에서 원소를 하나씩 제거하면서 출력
    print("Dequeue:", queue.dequeue())


print("큐가 비어 있음:", queue.isEmpty())