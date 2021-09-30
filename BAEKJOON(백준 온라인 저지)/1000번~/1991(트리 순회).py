# 1991 / 트리 순회 / S1
# https://www.acmicpc.net/problem/1991

class Node : # 트리를 배치하기 위한 클래스 Node 선언 및 구현
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node) : # 전위 순회 preorder 정의 함수
    # 전위 순회는 중-좌-우 순으로 순회됨

    # 중 출력
    print(node.item, end='')

    # 왼쪽 노드가 비어 있지 않는다면 preorder을 재귀 함수로 사용하여 왼쪽에 삽입 시킴
    if node.left != '.' :
        preorder(tree[node.left])
    
    # 오른쪽쪽 노드가 비어 있지 않는다면 preorder을 재귀 함수로 사용하여 오른쪽에 삽입 시킴
    if node.right != '.' :
        preorder(tree[node.right])

def inorder(node) : # 중위 순회 inorder 정의 함수
    # 중위 순회는 좌-중-우 순으로 순회됨

    # 왼쪽 노드가 비어 있지 않는다면 inorder을 재귀 함수로 사용하여 왼쪽에 삽입 시킴
    if node.left != '.' :
        inorder(tree[node.left])
    
    # 중 출력
    print(node.item, end='')

    # 오른쪽쪽 노드가 비어 있지 않는다면 inorder을 재귀 함수로 사용하여 오른쪽에 삽입 시킴
    if node.right != '.' :
        inorder(tree[node.right])

def postorder(node) : # 후위 순회 postorder 정의 함수
    # 후위 순회는 좌-우-중 순으로 순회됨

    # 왼쪽 노드가 비어 있지 않는다면 postorder을 재귀 함수로 사용하여 왼쪽에 삽입 시킴
    if node.left != '.' :
        postorder(tree[node.left])
    
    # 오른쪽쪽 노드가 비어 있지 않는다면 postorder을 재귀 함수로 사용하여 오른쪽에 삽입 시킴
    if node.right != '.' :
        postorder(tree[node.right])

    # 중 출력
    print(node.item, end='')

if __name__ == "__main__" :
    # 노드의 개수 입력
    N = int(input())
    # tree 리스트 선언
    tree = {}

    # 한 줄 마다 중 좌 우 순으로 입력 받고 그것을 리스트 tree에 삽입
    for _ in range(N) :
        node, left, right = map(str, input().split())
        tree[node] = Node(item = node, left = left, right = right)

    # 전위 순회 출력
    preorder(tree['A'])
    print()

    # 중위 순회 출력
    inorder(tree['A'])
    print()

    # 후위 순회 출력
    postorder(tree['A'])
    print()