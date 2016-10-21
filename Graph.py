class Graph:
    def __init__(self,nodes=None,edges=None):
        """Initialize a graph object.
        Args:
            nodes:  Iterator of nodes. Each node is an object.
            edges:  Iterator of edges. Each edge is a tuple of 2 nodes.
        """
        self.nodes,self.adj=[],{}
        if nodes!=None:
            self.add_nodes_from(nodes)
        if edges!=None:
            self.add_edges_from(nodes)
    def __len__(self):
        return len(self.nodes)

    def __contains__(self,x):
        return x in self.nodes
    def __iter__(self):
        return iter(self.nodes)
    def __getitem__(self,x):
        return iter(self.adj[x])
    def __str__(self):
        return 'V: %s\nE: %s' % (self.nodes,self.adj)
    def add_node(self,n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n]=[]
    def add_nodes_from(self,i):
        for n in i:
            self.add_node(n)
    def add_edge(self,u,v):
        self.adj[u]=self.adj.get(u,[])+[v]
        self.adj[v]=self.adj.get(v,[])+[u]

    def add_edges_from(self,i):
        for n in i:
            self.add_edge(*n)
    def number_of_nodes(self):
        return len(self.nodes)
    def number_of_edges(self):
        return sum(len(l) for _, l in self.adj.items())//2

class DGraph(Graph):
    def add_edge(self,u,v):
        self.adj[u]=self.adj.get(u,[])+[v]
class WGraph(Graph):
    def __init__(self,nodes=None,edges=None):
        self.weight = {}
        super(WGraph,self).__init__(nodes=None,edges=None)
    def add_edge(self,u,v,w):
        super(WGraph,self).add_edge(u,v)
        self.weight[(u,v)] = w
        self.weight[(v,u)] = w
    def get_weight(self,u,v):
        return self.weight[(u,v)]
class DWGraph(WGraph):
    def add_edge(self,u,v,w):
        self.adj[u]=self.adj.get(u,[])+[v]
        self.weight[(u,v)] = w


    def dfs(g,src):
        """Initialize a depth first search from vertex src on graph g.
        Args:
            g:      Graph to perform depth first search on.
            src:    Source vertex.
        Returns:
            Dictionary of paths.
        Raises:
            KeyError:   When source vertex is not in the graph.
        >>> V = [x for x in range(8)]
        >>> E = [(0,1), (0,2), (0,5), (0,6), (5,3), (5,4), (3,4), (6,4), (3,7)]
        >>> g = Graph(nodes=V, edges=E)
        >>> print(g)
        V: [0, 1, 2, 3, 4, 5, 6, 7]
        E: {0: [1, 2, 5, 6], 1: [0], 2: [0], 3: [5, 4, 7], 4: [5, 3, 6], 5: [0, 3, 4], 6: [0, 4], 7: [3]}
        >>> print(dfs(g, 0)[7])
        [0, 5, 3, 7]
        """
        mark={}
        prev={}
        for node in g:
            mark[node]=False
            prev[node]=None

        __dfs(g,src,mark,prev)
        paths={}
        for n in g:
            if not mark[n]: # n cannot be reached
                path[n]=None
                break
            path,dst=[],n # find path from src to n
            while dst!=src:
                path.append(dst)
                dst=prev[dst]
            path.append(src)
            paths[n] = list(reversed(path))
        return paths

    def __dfs(g,node,mark,prev):
        """Perform a depth first search based on the given graph and source vertex.
        Called when object is initialized.
        Args:
            node:   Node to recursively visit.
        Raises:
            KeyError:   When node is not in the graph.
        """
        mark[node]=True
        for n in g[node]:
            if not mark[n]:
                prev[n]=node
                __dfs(g,n,mark,prev)






#A Straightforward Adjacency List Representation
a,b,c,d,e,f,g,h=range(8)
N=[
    [b,c,d,e,f],
    [c,e],
    [d],
    [e],
    [f],
    [c,g,h],
    [f,h],
    [f,g]
]
#A Straightforward Adjacency Set Representation, O(1)
a,b,c,d,e,f,g,h=range(8)
N=[
    {b,c,d,e,f},
    {c,e},
    {d},
    {e},
    {f},
    {c,g,h},
    {f,h},
    {f,g}
]
#A Straightforward Adjacency dict with weighted edge
a,b,c,d,e,f,g,h=range(8)
N=[
    {b:2,c:1,d:3,e:9,f:4}
    {c:4,e:3},
    {d:8},
    {e:7},
    {f:5},
    {c:2,g:2,h:2},
    {f:1,h:6},
    {f:9,g:8}
]



    

def walk(G,s,S):
    P,Q=dict(),set()
    P[s]=None
    Q.add(s)
    while Q:
        u=Q.pop()
        for v in G[u].difference(P,S):
            Q.add(n)
            P[v]=u
    return P
def components(G,S):
    comp=[]
    seen=set()
    for u in G:
        if u in seen: continue
        C=walk(G,u,S)
        seen.update(u)
        comp.append(C)
    return comp
def rec_dfs(G,s,S=None):
    if S is None: S=set()
    S.add(s)
    for u in G[s]: 
    # when the path end, the recursion will end and the point
    # immediately jump to the last node which has more than one
    # edges. 
        if u in S: continue
        rec_dfs(G,u,S)
    return S

def traverse(G,s,qtype=set):
    # qtype can be every possible group type but you should define add 
    # accordingly
    # class stack(list):
    #   add=list.append
    S,Q=set(),qtype()
    Q.add(s)
    while Q:
        u=Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u 

def dfs_time(G,s,d,f,S=None,t=0):
    #dfs with timestamps
    if S is None: S=set()
    d[s]=t;t+=1
    S.add(s)
    for u in G[s]:
        if u in S:continue
        t=dfs_time(G,u,d,f,S,t)
    f[s]=t;t+=1
    return t
def traverse(G,s,d,f,qtype=set,t=0):
    S,Q =set(),qtype()
    Q.add(s)
    while Q:
        u=Q.pop()[1]
        if not u:
            f[u]=t;t+1
            yield t
        if u in S: continue
        S.add(u)
        d[u]=t;t+1
        Q.add((u,None))
        for v in G[u]:
            Q.add((u,v))

def dfs_topsort(G):
    S,res=set(),[]
    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse[v]
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res
def iddfs(G,s):
    yielded=set()
    def recurse(G,s,d,S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d==0:return
        if S is None: S=set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurse(G,s,d-1,S):
                yield v
    n=len(G):
    for d in range(n):
        if len(yielded)==n:break
        for u in recurse(G,s,d):
            yield u
from collections import deque
def bfs(G,s):
    P,Q={s:None},deque([s])
    while Q:
        u=Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v]=u
            Q.append(v)
    return P

def tr(G):
    GT={}
    for u in G:GT[u]=set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT=tr(G)
    sccs,seen=[],set()
    for u in dfs_topsort(G):
        if u in seen: continue
        C=walk(GT,u,seen)
        seen.update(C)
        sccs.append(C)
    return sccs

from string import ascii_lowercase
def parse_graph(s):
    G={}
    for u, line in zip(ascii_lowercase,s.split("/")):
        G[u]=set(line)
    return G








