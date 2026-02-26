class Solution {
  public:
    int majorityElement(vector<int>& arr) {
        // code here
        unordered_map<int, int>umap;
        int majority = arr.size()/2;
        for(int num: arr){
            umap[num]++;
        }
        for(int num: arr){
            if(umap[num] > majority){
                return num;
            }
        }
        return -1;
    }
};