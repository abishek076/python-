class graph:
    def __init__(self):
        self.g={}
    def create(self,u,v,price):
        obj.add_vertex(u,v)
        obj.add_edge(u,v,price)
    def add_vertex(self,u,v):
        if u not in self.g:
            self.g[u]=[]
        if v not in self.g:
            self.g[v]=[]
    def add_edge(self,u,v,price):
        if u not in self.g:
            print(None)
        elif v not in self.g:
            print(None)
        else:
            self.g[u].append((v,price))
    def display(self):
        print(self.g)
    def bfs(self,start):
        l={}
        for i in sorted(self.g):
            if i not in l:
                if i==start:
                    l[i]=0
                else:
                    l[i]=float('inf')
        visited=set()
        queue=[start]
        result=[]
        while queue:
            v=queue.pop(0)
            if v not in visited:
                visited.add(v)
                result.append(v)
                for j in self.g[v]:
                    if self.g[j[0]] is not None:
                        if j[0] not in visited:
                            queue.append(j[0])
                            l[j[0]]=min(l[j[0]],l[v]+j[1])
        return l
obj=graph()
while True:
    l=list(map(int,input().split()))
    if l:
        obj.create(l[0],l[1],l[2])
    else:
        break
src=int(input("src"))
obj.display()
k=obj.bfs(src)
print(k)