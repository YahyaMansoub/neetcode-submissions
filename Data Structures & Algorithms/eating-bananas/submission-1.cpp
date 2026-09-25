class Solution {
public:

    long long calc(const vector<int>& piles, int k){
        long long h=0; 

        for(int pile: piles){
            h += (pile+k-1LL)/k; 

        }
        return h; 
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int l =1; 
        int high = *max_element(piles.begin(), piles.end()); 
        int ans = high;

        while(l<=high){
            int k = (l+high)/2; 
            long long hours = calc(piles, k); 

            if(hours<=h){
                ans = k; 
                high=k-1; 
            }else{

                l = k+1; 
            }
        }  

        return ans; 
    }
};
