class Solution {
  public:
    // Function to find all elements in array that appear more than n/k times.
    int countOccurence(vector<int>& arr, int k) {
        // Your code here
        unordered_map<int, int>umap;
        int max_ele = arr.size()/k;
        int count = 0;
        for(int num: arr){
            umap[num]++;
        }
        for(auto it: umap){
            if(it.second > max_ele){
                count++;
            }
        }
        return count;
    }
};