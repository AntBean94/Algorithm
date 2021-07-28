# 15강 이진 트리

## 이진 트리(Binary Tree)의 구현과 순회(Traversal) 방식

## 전위 순회, 중위 순회, 후위 순회

---





---

**Python**

```python

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

