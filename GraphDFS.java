import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;
import java.util.Vector;

/**
 * Graph
 */
@SuppressWarnings({ "unchecked" })
public class GraphDFS {
    static class Graph {
        int V;
        static LinkedList<Integer>[] adj = null;

        Graph(int V) {
            this.V = V;
            adj = new LinkedList[V];
            for (int i = 0; i < adj.length; i++) {
                adj[i] = new LinkedList<Integer>();
            }
        }

        void addEdge(int v, int w) {
            adj[v].add(w);
        }

        public void printGraph() {
            for (int i = 0; i < V; i++) {
                if (adj[i].size() > 0) {
                    System.out.print("Cạnh " + i + " được kết nối với các cạnh: ");
                    for (int j = 0; j < adj[i].size(); j++) {
                        System.out.print(adj[i].get(j) + " ");
                    }
                    System.out.println();
                }
            }
        }

        public void DFS_Recursion(int v) {
            boolean[] v_visited = new boolean[V];
            DFS(v, v_visited);
        }

        public void DFS(int v_start, boolean[] visited) {
            visited[v_start] = true;
            System.out.print(v_start + " ");
            for (int i = 0; i < adj[v_start].size(); i++) {
                int des = adj[v_start].get(i);
                if (!visited[des]) {
                    DFS(des, visited);
                }
            }
        }

        void DFS_non_Recursion(int s){ 
            Vector<Boolean> visited = new Vector<Boolean>(V); 
            for (int i = 0; i < V; i++){
                visited.add(false);
            }
            Stack<Integer> stack = new Stack<>(); 
            stack.push(s);
            while(stack.empty() == false) { 
                s = stack.peek(); 
                stack.pop(); 
                if(visited.get(s) == false){ 
                    System.out.print(s + " "); 
                    visited.set(s, true); 
                } 
                Iterator<Integer> ite = adj[s].iterator(); 
                while (ite.hasNext()){ 
                    int v = ite.next(); 
                    if(!visited.get(v)) 
                        stack.push(v); 
                } 
            } 
        }
    }

    private static int input() {
        int n = 0;
        try {
            Scanner sc = new Scanner(System.in);
            n = sc.nextInt(); 
        }
        catch(Exception d) {
            Scanner sc = new Scanner(System.in);
            System.out.print("Nhập lỗi!\nHãy nhập lại!: ");
            n = sc.nextInt();
        }
        return n;
    }

    public static void main(String[] args) {
        System.out.print("Nhập đỉnh cho đồ thị: ");
        int V=input();
        Graph g = new Graph(V);
        for (int i = 0; i < V; i++) {
            System.out.print("Nhập số cạnh của đỉnh "+i+": ");
            int E=input();
            for (int j = 0; j < E; j++) {
                System.out.print("Ta có cạnh từ đỉnh "+i+" đến đỉnh: ");
                int n=input();
                g.addEdge(i, n);
            }
        }
        g.printGraph();
        System.out.print("Nhập đỉnh xuất phát để duyệt: ");
        int vstart = input();
        System.out.print("Kết quả duyệt chiều sâu dùng đệ quy:");
        g.DFS_Recursion(vstart);
        System.out.print("\nKết quả duyệt chiều sâu Không dùng đệ quy:");
        g.DFS_non_Recursion(vstart);
    }

}


