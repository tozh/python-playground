import sys

def prim(graph,n):
    dis=[0]*n
    flag=[False]*n
    flag[0]=True
    k=0
    for i in range(n):
        dis[i]=graph[k][i]
    for j in range(n-1):
        mini = float('inf')
        for i in range(n):
            if mini>dis[i] and not flag[i]:
                mini=dis[i]
                k=i
        if k==0:#不连通
            return
        flag[k]=True
        for i in range(n):
            if dis[i]>graph[k][i] and not flag[i]:
                dis[i]=graph[k][i]
    return dis

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip().split(' ', 1)
    N = int(line1[0])
    M = int(line1[1])

    mat = [[float('inf') for _ in range(N)] for j in range(N)]
    for i in range(M):
        # 读取每一行
        line = sys.stdin.readline().strip().split(' ')
        P = int(line[0])
        Q = int(line[1])
        K = int(line[2])
        mat[P-1][Q-1] = K
        mat[Q - 1][P - 1] = K
    dis = prim(mat, N)
    ans = float('-inf')
    for val in dis:
        if val != float('inf'):
            ans = val if val > ans else ans
    print(ans)


