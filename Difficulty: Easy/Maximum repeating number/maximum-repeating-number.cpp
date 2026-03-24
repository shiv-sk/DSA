// User function template for C++
class Solution {
  public:
    // Returns maximum repeating element in arr[0..n-1].
    // The array elements are in range from 0 to k-1
    int maxRepeating(int k, vector<int>& arr) {
        // code here
        int max_repeating_number = -1;
        int max_count = -1;
        unordered_map<int, int>umap;
        for(int num: arr){
            umap[num]++;
        }
        for(int num: arr){
            int current_count = umap[num];
            if(current_count > max_count){
                max_repeating_number = num;
                max_count = current_count;
            }
            else if(current_count == max_count){
                max_repeating_number = min(num, max_repeating_number);
            }
        }
        return max_repeating_number;
    }
};