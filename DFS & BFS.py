graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# DFS use recursive
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


# DFS use stack
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


test = []
print(recursive_dfs(1, test))
print(iterative_dfs(1))
# 같은 DFS이지만 순서가 다르다
# 이유는 스택으로 구현하면 스택에 담긴 가장 최근 노드, 즉 가장 마지막 부터 방문하기 떄문이다.
# 구현 방식에 따라 이 점을 주의
