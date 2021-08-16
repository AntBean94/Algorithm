# 크루스칼 알고리즘 (Kruskal Algorithm) 예제

# unionfind 구현
def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a < b: parent[b] = a
    else: parent[a] = b

def findParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a == b: return True
    else: return False

# kruskal 알고리즘 구현
def kruskal(graph, min_tree, node):
    graph.sort(key=lambda x: x[2])

    value = 0
    line_num = node - 1
    key = 0
    while line_num > 0:
        a = graph[key][0]
        b = graph[key][1]
        if findParent(min_tree, a, b):
            key += 1
        else:
            unionParent(min_tree, a, b)
            print(graph[key][2])
            value += graph[key][2]
            line_num -= 1
            key += 1
    return value

# 노드의 갯수
node = 7
# 최소신장 트리
min_tree = [i for i in range(node+1)]
# 간선 정보
graph = [[1, 7, 12],
        [1, 4, 28],
        [1, 2, 67],
        [1, 5, 17],
        [2, 4, 24],
        [2, 5, 62],
        [3, 5, 20],
        [3, 6, 37],
        [4, 7, 13],
        [5, 6, 45],
        [5, 7, 73]]

print(kruskal(graph, min_tree, node))
print(min_tree)