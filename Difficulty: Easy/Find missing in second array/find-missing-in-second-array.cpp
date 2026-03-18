class Solution {

  public:
    vector<int> findMissing(vector<int>& a, vector<int>& b) {
        // Your code goes here
        unordered_set<int>u_set(b.begin(), b.end());
        vector<int>ans;
        
        for(int num : a){
            if(u_set.find(num) == u_set.end()){
                ans.push_back(num);
            }
        }
        return ans;
    }
};
