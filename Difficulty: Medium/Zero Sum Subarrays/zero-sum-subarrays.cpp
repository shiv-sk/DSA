class Solution {
  public:
    int findSubarray(vector<int> &arr) {
        // code here.
        unordered_map<int, int>umap;
        umap[0] = 1;
        int sum = 0;
        int total = 0;
        for(int num : arr){
            sum += num;
            if(umap.find(sum) != umap.end()){
                total = total + umap[sum];
            }
            umap[sum]++;
        }
        return total;
    }
};