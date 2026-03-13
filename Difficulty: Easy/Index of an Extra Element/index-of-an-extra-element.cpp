class Solution {
  public:
    int findExtra(vector<int>& a, vector<int>& b) {
        // add code here.
        for(int i = 0; i < b.size(); i++){
            if(a[i] != b[i]){
                return i;
            }
        }
        return a.size()-1;
    }
};