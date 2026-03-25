// User function Template for C++

class Solution {
  public:
    vector<int> increment(vector<int> arr, int N) {
        // code here
        for(int i = arr.size()-1; i >= 0; i--){
            if(arr[i] == 9){
                arr[i] = 0;
            }
            else{
                arr[i] += 1;
                break;
            }
            
        }
        vector<int>ans(arr.size()+1, 0);
        if(arr[0] == 0){
            ans[0] = 1;
            return ans;
        }
        return arr;
    }
};