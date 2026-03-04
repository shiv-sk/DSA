class Solution {
  public:
    vector<int> removeDuplicates(vector<int> &arr) {
        // code here
        int left = 0;
        int right = 1;
        vector<int> ans;
        while(right < arr.size()){
            if(arr[left] != arr[right]){
                arr[left+1] = arr[right];
                left++;
            }
            right++;
        }
        for(int i = 0; i <= left; i++){
            ans.push_back(arr[i]);
        }
        return ans;
    }
};