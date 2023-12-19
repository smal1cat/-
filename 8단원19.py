class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_complete_binary_tree(root):
    if not root:
        return True  # 루트가 없으면 완전 이진 트리입니다.

    queue = [root]
    found_null = False  # None을 발견했는지 여부를 나타내는 변수

    while queue:
        current_node = queue.pop(0)

        if not current_node:
            found_null = True  # 현재 노드가 None인 경우, None을 발견했다고 표시
        else:
            if found_null:
                return False  # 이미 None을 발견한 이후에 노드가 나오면 완전 이진 트리가 아닙니다.

            # 현재 노드의 자식 노드들을 큐에 추가
            queue.append(current_node.left)
            queue.append(current_node.right)

    return True  # 큐가 비어서 끝났을 때까지 None을 발견하지 않았으면 완전 이진 트리입니다.