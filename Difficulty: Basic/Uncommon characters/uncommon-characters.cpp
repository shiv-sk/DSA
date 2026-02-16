class Solution {
  public:
    string uncommonChars(string& s1, string& s2) {
        // code here
        set<char> set1(s1.begin(), s1.end());
        set<char> set2(s2.begin(), s2.end());
        
        string result = "";
        for(char c: set1){
            if(set2.find(c) == set2.end()){
                result += c;
            }
        }
        
        for(char c: set2){
            if(set1.find(c) == set1.end()){
                result += c;
            }
        }
        sort(result.begin(), result.end());
        return result; 
    }
};
