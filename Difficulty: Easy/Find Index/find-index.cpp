class Solution {
  public:
    vector<int> findIndex(vector<int>& arr, int key) {
        // code here.
        int first = -1, last = -1;
        vector<int>ans(2, -1);
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == key){
                if(first == -1){
                    first = i;
                }
                last = i;
            }
        }
        ans[0] = first;
        ans[1] = last;
        return ans;
    }
};