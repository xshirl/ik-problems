#
# Complete the 'zombieCluster' function below.
#
# The function accepts STRING ARRAY as parameter.
#
def zombieCluster(zombies):
    visited = [False] * len(zombies)
    def dfs(z):
        visited[z] = True
        for friend in range(len(zombies[z])):
            if zombies[z][friend] == '1' and not visited[friend]:
                dfs(friend)
    count =0
    for i in range(len(zombies)):
        if not visited[i]:
            dfs(i)
            count += 1
    return count