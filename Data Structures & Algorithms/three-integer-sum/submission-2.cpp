class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        vector<vector<int>> sol;
        int l=0, r=0, sum =0; 
        for(int i=0; i< nums.size(); i++){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            l=i+1, r= nums.size()-1; 
            while(l < r){
                sum = nums[l]+nums[i]+nums[r]; 
                if (sum==0){
                    sol.push_back({nums[l], nums[i], nums[r]}); 
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;


                }else if(sum > 0){
                      r--; 
                }else{
                    l++; 
                }

            }
        }
        return sol; 
    }
};
