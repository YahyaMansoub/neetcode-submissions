class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l=0,  m=0, row=0, col=0;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int r = rows * cols - 1;


        while (l<=r){
            m = (l+r)/2; 
            row=m/cols; 
            col = m%cols; 

            if(target==matrix[row][col]){
                return true; 
            }else if (target>matrix[row][col]){
                l=m+1; 
            }else{
                r=m-1; 
            }

        }

        return false; 
    }
};
