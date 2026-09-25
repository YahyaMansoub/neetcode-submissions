class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        stack<int> indices;
        int n=temperatures.size();
        vector<int> sol(n);
        for(int i=0; i<n;i++){
            if(indices.empty()){
                indices.push(i);
                continue;
            }
            if (temperatures[indices.top()] >= temperatures[i]){
               indices.push(i);
            }else{
               while(!indices.empty() &&
       temperatures[indices.top()] < temperatures[i]){
                sol[indices.top()]=i-indices.top();
                indices.pop();
               }
               indices.push(i);
            }

        }
        return sol;
    }
};
