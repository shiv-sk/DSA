// User function Template for C++

class Solution {
  public:
    // Function to find maximum value among the difference of element and index.
    int maxVal(vector<int> &arr) {
        // code here
        int max_ele = INT_MIN;
        int min_ele = INT_MAX;
        for(int i = 0; i < arr.size(); i++){
            int val = arr[i] - i;
            max_ele = max(max_ele, val);
            min_ele = min(min_ele, val);
        }
        return max_ele - min_ele;
    }
};