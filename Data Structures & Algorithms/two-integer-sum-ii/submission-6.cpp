class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0, r=numbers.size()-1; 
        int sum=0; 
        vector<int> sol;

        while(l<r){
             sum = numbers[r]+numbers[l]; 

             if(sum == target){
                return {l+1, r+1};

             }else if(sum > target){
                r--; 
             }else{
                l++;
             }
        }

        return {}; 

        


    }
};
