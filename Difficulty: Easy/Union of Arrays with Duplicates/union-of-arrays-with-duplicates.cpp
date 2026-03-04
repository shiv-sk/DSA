class Solution {
  public:
    vector<int> findUnion(vector<int>& a, vector<int>& b) {
        // code here
        unordered_set<int>uset;
        for(int num : a){
            uset.insert(num);
        }
        for(int num : b){
            uset.insert(num);
        }
        vector<int>ans(uset.begin(), uset.end());
        return ans;
    }
};