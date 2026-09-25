class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> indices;

        int n = temperatures.size();
        vector<int> sol(n, 0);

        for (int i = 0; i < n; i++) {

            while (!indices.empty() &&
                   temperatures[indices.top()] < temperatures[i]) {

                int prev = indices.top();
                indices.pop();

                sol[prev] = i - prev;
            }

            indices.push(i);
        }

        return sol;
    }
};