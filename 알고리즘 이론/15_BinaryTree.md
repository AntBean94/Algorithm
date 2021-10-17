# 15강 이진 트리

## 이진 트리(Binary Tree)의 구현과 순회(Traversal) 방식

## 전위 순회, 중위 순회, 후위 순회

---
1. 전위 순회(Preorder)
- 노드를 방문한다.
- 왼쪽 서브 트리를 전위 순회한다.
- 오른쪽 서브 트리를 전위 순회한다.
=> 깊이 우선 순회(depth-first traversal)라고도 한다.

2. 중위 순회(Inorder)
- 왼쪽 서브 트리를 중위 순회한다.
- 노드를 방문한다.
- 오른쪽 서브 트리를 중위 순회한다.
=> 대칭 순회(symmetric)라고도 한다.

3. 후위 순회(Postorder)
- 왼쪽 서브 트리를 후위 순회한다.
- 오른쪽 서브 트리를 후위 순회한다.
- 노드를 방문한다.

4. 레벨 순서 순회(level-order)
- 모든 노드를 낮은 레벨부터 차례대로 순회한다.
- 너비 우선 순회(breadth-first traversal)라고도 한다.
---

**Python**

```python
# 15강 이진트리 구현, 순회 예제

# 노드 생성
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 노드 삽입
class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

# 노드 탐색
def search(self, value):
    self.current_node = self.root
    while self.current_node:
        if self.current_node.value == value:
            return True
        elif self.current_node.value > value:
            self.current_node = self.current_node.left
        else:
            self.current_node = self.current_node.right
    return False

# 노드 삭제
def delete(self, value):
    # 삭제할 노드가 있는지 검사하고 없으면 False 리턴
    # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
    is_search = False
    self.current_node = self.root
    self.parent = self.root
    while self.current_node:
        if self.current_node.value == value:
            is_search = True
            break
        elif value < self.current_node.value:
            self.parent = self.current_node
            self.current_node = self.current_node.left
        else:
            self.parent = self.current_node
            self.current_node = self.current_node.right
    if is_search == False:
        return False

    # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
    if self.current_node.left == None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = None
        else:
            self.parent.right = None
    
    # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
    if self.current_node.left != None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = self.current_node.left
        else:
            self.parent.right = self.current_node.left
    
    # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
    if self.current_node.left == None and self.current_node.right != None:
        if value < self.parent.value:
            self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right                

    # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
    if self.current_node.left != None and self.current_node.right != None:
        self.change_node = self.current_node.right
        self.change_node_parent = self.current_node.right
        while self.change_node.left != None:
            self.change_node_parent = self.change_node
            self.change_node = self.change_node.left
        if self.change_node.right != None:
            self.change_node_parent.left = self.change_node.right
        else:
            self.change_node_parent.left = None
            
        if value < self.parent.value:
            self.parent.left = self.change_node
            self.change_node.right = self.current_node.right
            self.change_node.left = self.current_node.left
        else:
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right

    return True     
```



**C++**

```C++
#include <iostream>

using namespace std;

int number = 15;

// 하나의 노드 정보를 선언합니다.
typedef struct node *treePointer;
typedef struct node {
  int data;
  treePointer leftChild, rightChild;
} node;

// 전위 순회를 구현합니다.
void preorder(treePointer ptr) {
  if(ptr) {
    cout << ptr->data << ' ';
    preorder(ptr->leftChild);
    preorder(ptr->rightChild);
  }
}

// 중위 순회를 구현합니다.
void inorder(treePointer ptr) {
  if(ptr) {}
    preorder(ptr->leftChild);
  	cout << ptr->data << ' ';
    preorder(ptr->rightChild);
  }
}

// 후위 순회를 구현합니다.
void postorder(treePointer ptr) {
  if(ptr) {
    preorder(ptr->leftChild);
    preorder(ptr->rightChild);
    cout << ptr->data << ' ';
  }
}

int main(void) {
  node nodes[number + 1];
  for(int i = 1; i <= number; i++) {
    nodes[i].data = i;
    nodes[i].leftChild = NULL;
    nodes[i].rightChild = NULL;
  }
  for(int i = 1; i <= number; i++) {
    if(i % 2 == 0) {
      nodes[i / 2].leftChild = &nodes[i];
    }
    else {
      nodes[i / 2].rightChild = &nodes[i];
    }
  }
  preorder(&nodes[1]);
	inorder(&nodes[1]);
  postorder(&nodes[1]);
  return 0;
}
```

