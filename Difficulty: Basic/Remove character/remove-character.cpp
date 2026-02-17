// User function template for c++
class Solution {
  public:
    string removeChars(string str1, string str2) {
        // code here
        string new_str = "";
        unordered_map<char, int>umap;
        for(char ch: str2){
            umap[ch]++;
        }
        for(char c: str1){
            if(umap.find(c) == umap.end()){
                new_str += c;
            }
        }
        return new_str;
    }
};
