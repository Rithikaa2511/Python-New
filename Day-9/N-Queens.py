class Solution(object):
    def solveNQueens(self, n):
        res=[]
        board=[]
        for i in range(n):
            r=[]
            for i in range(n):
                r.append('.')
            board.append(r)
        left=[0]*n
        upper=[0]*(2*n-1)
        lower=[0]*(2*n-1)
        self.solve(0,res,board,left,upper,lower)
        return res
    def solve(self,col,res,board,left,upper,lower):
        n=len(board)
        if(col==n):
            temp=[]
            for j in range(n):
                temp.append("".join(board[j]))
            res.append(temp)
            return
        for i in range(n):
            if(left[i]==0 and upper[n-1+col-i]==0 and lower[col+i]==0):
                board[i][col]='Q'
                left[i]=1
                upper[n-1+col-i]=1
                lower[col+i]=1
                self.solve(col+1,res,board,left,upper,lower)
                board[i][col]='.'
                left[i]=0
                upper[n-1+col-i]=0
                lower[col+i]=0
