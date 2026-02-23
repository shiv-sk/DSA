class Solution {
  public:
    bool isPalindrome(string& s) {
        // code here
        int left_char = 0;
        int right_char = s.size()-1;
        
        while(left_char < right_char){
            if(s[left_char] != s[right_char]){
                return false;
            }
            left_char++;
            right_char--;
        }
        return true;
    }
};