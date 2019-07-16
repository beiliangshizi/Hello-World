# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 小青蛙有一天不小心落入了一个地下迷宫,小青蛙希望用自己仅剩的体力值P跳出这个地下迷宫。为了让问题简单,
# 假设这是一个n*m的格子迷宫,迷宫每个位置为0或者1,0代表这个位置有障碍物,小青蛙达到不了这个位置;
# 1代表小青蛙可以达到的位置。小青蛙初始在(0,0)位置,地下迷宫的出口在(0,m-1)
# (保证这两个位置都是1,并且保证一定有起点到终点可达的路径),小青蛙在迷宫中水平移动一个单位距离需要消耗1点体力值,
# 向上爬一个单位距离需要消耗3个单位的体力值,向下移动不消耗体力值,当小青蛙的体力值等于0的时候还没有到达出口,
# 小青蛙将无法逃离迷宫。现在需要你帮助小青蛙计算出能否用仅剩的体力值跳出迷宫(即达到(0,m-1)位置)。
# 输入描述:
# 输入包括n+1行:
#
# 第一行为三个整数n,m(3 <= m,n <= 10),P(1 <= P <= 100)
#
# 接下来的n行:
#
# 每行m个0或者1,以空格分隔
# 输出描述:
# 如果能逃离迷宫,则输出一行体力消耗最小的路径,输出格式见样例所示;如果不能逃离迷宫,则输出"Can not escape!"。
# 测试数据保证答案唯一
# 示例1
# 输入
#
# 4 4 10
# 1 0 0 1
# 1 1 0 1
# 0 1 1 1
# 0 0 1 1
# 输出
#
# [0,0],[1,0],[1,1],[2,1],[2,2],[2,3],[1,3],[0,3]

def backtracking(maze, P_map, i, j, P, m, n, curPath, final):
    if i == 0 and j == m - 1:
        if not final:
            final.append(curPath)
        elif final and len(final[0]) > len(curPath):
            final[0] = curPath
        return
    if P < 0:
        return

    if 0 <= i - 1 and maze[i - 1][j] and P - 3 > P_map[i - 1][j]:
        P_map[i - 1][j] = P - 3
        backtracking(maze, P_map, i - 1, j, P - 3, m, n, curPath + [[i - 1, j]], final)
    if i + 1 < n and maze[i + 1][j] and P > P_map[i + 1][j]:
        P_map[i + 1][j] = P
        backtracking(maze, P_map, i + 1, j, P, m, n, curPath + [[i + 1, j]], final)
    if 0 <= j - 1 and maze[i][j - 1] and P - 1 > P_map[i][j - 1]:
        P_map[i][j - 1] = P - 1
        backtracking(maze, P_map, i, j - 1, P - 1, m, n, curPath + [[i, j - 1]], final)
    if j + 1 < m and maze[i][j + 1] and P - 1 > P_map[i][j + 1]:
        P_map[i][j + 1] = P - 1
        backtracking(maze, P_map, i, j + 1, P - 1, m, n, curPath + [[i, j + 1]], final)


n, m, P = map(int, raw_input().split())
maze = []
for i in range(n):
    maze.append(map(int, raw_input().split()))
P_map = [[-1] * m for i in range(n)]
P_map[0][0] = P
final = []
backtracking(maze, P_map, 0, 0, P, m, n, [[0, 0]], final)
if not final:
    print 'Can not escape!'
else:
    ans = '[' + str(final[0][0][0]) + ',' + str(final[0][0][1]) + ']'
    for i in range(1, len(final[0])):
        ans += ',' + '[' + str(final[0][i][0]) + ',' + str(final[0][i][1]) + ']'
    print ans