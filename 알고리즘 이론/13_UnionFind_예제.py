# 합집합 찾기 (Union-Find) 예제

parent = [i for i in range(11)]

# 부모 노드를 찾는 함수
def getParent(parent, x):
    if parent[x] == x: return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 두 부모 노드를 합치는 함수
def unionParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 같은 부모를 가지는지 확인
def findParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a==b:
        return True
    else:
        return False
    
unionParent(parent, 1, 2)
unionParent(parent, 2, 3)
unionParent(parent, 3, 4)
unionParent(parent, 5, 6)
unionParent(parent, 6, 7)
unionParent(parent, 7, 8)
print(f"1과 5는 연결되어있나요? {findParent(parent, 1, 5)}")
unionParent(parent, 1, 5)
print(f"1과 5는 연결되어있나요? {findParent(parent, 1, 5)}")
