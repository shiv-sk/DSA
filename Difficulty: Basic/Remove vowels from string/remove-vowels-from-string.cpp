// User function template for C++
class Solution {
  public:

    string removeVowels(string& s) {
        // Your code goes here
        string result = "";
        for(char c : s){
            if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u'){
                result += c;
            }
        }
        return result;
    }
};