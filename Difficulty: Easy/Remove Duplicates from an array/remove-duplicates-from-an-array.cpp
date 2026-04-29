class Solution {
  public:
    vector<int> remDuplicate(vector<int>& arr) {
        // code here
        sort(arr.begin(), arr.end());
        for(int i = 0; i < arr.size()-1; i++){
            if(arr[i] == arr[i+1]){
                arr.erase(arr.begin() + i);
                i--;
            }
        }
        return arr;
    }
};