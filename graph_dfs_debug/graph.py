"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Cannot put an edge on a nonexistent vertex")
        else:
            self.vertices[start].add(end)
            start.component += 1
            if bidirectional:
                self.vertices[end].add(start)
                end.component += 1

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            cur_node = stack.pop()
            if cur_node == target:
                break
            visited.add(cur_node)
            stack.extend(self.vertices[cur_node] - visited)
        return visited

    def graph_rec(self, start, target=None):
        x = set()
        x.add(start)
        for v in self.vertices[start]:
            self.graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
