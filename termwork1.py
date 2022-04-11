#basic
stack =[]

stack.append('a')
stack.append('b')
stack.append('c')

print(f"Initial stack {stack}")


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(f"stack after element popped: {stack}")


queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

print(f"Initial queue {queue}")

print(queue.pop())
print(queue.pop())
print(queue.pop())

print(f"queue after element popped: {queue}")

#DFS

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()

        self.DFSUtil(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
print("\n")
print("Following is Depth First Traversal (starting from vertex 2)")
g.DFS(2)


# main program

graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E' , 'F'],
    'D' : ['G' , 'H'],
    'E' : ['I' , 'J'],
    'F' : ['K' , 'L'],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : [],
    'K' : [],
    'L' : []

}

path = []
def IDDFS(root , goal):
        depth = 0
        while True:
                result = DLS(root , goal , depth)
                if result == goal:
                        return result
                depth = depth + 1


def DLS(node, goal, depth):
        if node not in path:
                path.append(node)
        if depth == 0 and  node == goal :
            print("------Found Goal , Returing -----")
            return node
        elif depth > 0:
            for child in graph.get(node, []):
                if goal == DLS(child , goal, depth-1):
                    return goal

IDDFS('A', 'J')
print(path)
