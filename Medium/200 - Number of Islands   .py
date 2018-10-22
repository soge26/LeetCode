#Method 1:

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if grid is None:
            return 0
        
        islands=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== '1':
                    islands+=1
                    self.islandDFS(grid,i,j)
        return islands

    def islandDFS(self,grid,i,j):
        if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j]!= '1':
            return
            
        grid[i][j]='x'
        self.islandDFS(grid,i+1,j)
        self.islandDFS(grid,i-1,j)
        self.islandDFS(grid,i,j+1)
        self.islandDFS(grid,i,j-1)

