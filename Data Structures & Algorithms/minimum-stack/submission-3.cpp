class MinStack {

private:
stack<pair<int, int>> stk;
public:
    MinStack() {
        
        
    }
    
    void push(int val) {
        int mini=val;
        if(!stk.empty()){
            mini=min(val, stk.top().second);
        }
        stk.push({val, mini});
    }
    
    void pop() {
        stk.pop();
    }
    
    int top() {
        return stk.top().first;
    }
    
    int getMin() {
        return stk.top().second;     
    }
};
