class Solution {
public:
    int characterReplacement(std::string s, int k) {
        std::vector<int> count(26, 0);
        int max_freq = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); ++right) {
            // 1. Add current character count
            count[s[right] - 'A']++;
            
            // 2. Update historical maximum frequency
            max_freq = std::max(max_freq, count[s[right] - 'A']);
            
            // 3. If replacements needed exceed k, shift the left boundary forward once
            if ((right - left + 1) - max_freq > k) {
                count[s[left] - 'A']--;
                left++;
            }
        }
        
        // The maximum valid window size achieved is the distance between right and left
        return s.length() - left;
    }
};