class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                brackets.push(c);
            } else {
                if (brackets.empty()) {
                    return false;
                }

                char opening = brackets.top();

                if ((c == ')' && opening != '(') ||
                    (c == ']' && opening != '[') ||
                    (c == '}' && opening != '{')) {
                    return false;
                }

                brackets.pop();
            }
        }

        return brackets.empty();
    }
};
