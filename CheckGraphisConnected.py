from collections import defaultdict as gdict
class Graph: 
  
    def __init__(self,vertices):
        self.V = vertices
        self.graph = gdict(list) 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
    def DFSUtil(self,v,visited):  
        visited[v]= True
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited)
    def reverseGraph(self): 
        g = Graph(self.V) 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g
    
    def Is_Connected(self): 
        visited =[False]*(self.V) 
        self.DFSUtil(0,visited) 
        if any(i == False for i in visited): 
            return False
        g = self.reverseGraph() 
        visited =[False]*(self.V) 
        g.DFSUtil(0,visited)  
        if any(i == False for i in visited): 
            return False
        return True
 
def main():
    g_default = Graph(5) 
    g_default.addEdge(0, 1) 
    g_default.addEdge(1, 2) 
    g_default.addEdge(2, 3) 
    g_default.addEdge(3, 0) 
    g_default.addEdge(2, 4) 
    g_default.addEdge(4, 2) 
    v = int(input("Nhập số đỉnh của đồ thị(Nhập 0 để dùng đồ thị mặc định): "))
    if v==0 :
        g = g_default
    else:
        g= Graph(v)
    for i in range(v):
        e=int(input('Nhập số cạnh của đỉnh %d: ' %i))
        for j in range(e):
            n=int(input("Ta có cạnh từ đỉnh %d đến đỉnh " %i))
            g.addEdge(i,n)
    print(g.graph)
    print("Đồ thị đã nhập có liên thông!") if g.Is_Connected() else print("Đồ thị đã nhập Không liên thông!")
        
    

if __name__ == "__main__":
    main()