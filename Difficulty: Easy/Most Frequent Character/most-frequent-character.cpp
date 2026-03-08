class Solution {
  public:
    char getMaxOccuringChar(string& s) {
        //  code here
        sort(s.begin(), s.end());
        vector<int> freq(26, 0);
        for(int i = 0; i < s.size(); i++){
            freq[s[i] - 'a']++;
        }
        int max_count = INT_MIN;
        char max_occuring = 'a';
        for(char ch : s){
            if(freq[ch - 'a'] > max_count){
                max_count = freq[ch - 'a'];
                max_occuring = ch;
            }
        }
        return max_occuring;
    }
};