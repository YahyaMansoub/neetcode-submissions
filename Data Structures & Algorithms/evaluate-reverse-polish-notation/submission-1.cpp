class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> values;

        for (const string& token : tokens) {
            if (token != "+" && token != "-" &&
                token != "*" && token != "/") {
                
                values.push(stoi(token));
                continue;
            }

            int right = values.top();
            values.pop();

            int left = values.top();
            values.pop();

            if (token == "+") {
                values.push(left + right);
            } else if (token == "-") {
                values.push(left - right);
            } else if (token == "*") {
                values.push(left * right);
            } else {
                values.push(left / right);
            }
        }

        return values.top();
    }
};