class Solution {
  public:
    vector<int> findTwoElement(vector<int>& arr) {
        // code here
        vector<int>ans(2, -1);
        unordered_map<int, int>umap;
        for(int num : arr){
            umap[num]++;
        }
        for(int i = 0; i < arr.size(); i++){
            if( umap[arr[i]] == 2 ){
                ans[0] = arr[i];
            }
            if( umap.find(i+1) == umap.end()){
                ans[1] = i+1;
            }
        }
        if(ans[1] == -1){
            ans[1] = arr.size();
        }
        return ans;
    }
};