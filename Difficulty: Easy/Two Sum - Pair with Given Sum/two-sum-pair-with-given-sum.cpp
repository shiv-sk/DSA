class Solution {
  public:
    bool twoSum(vector<int>& arr, int target) {
        // code here
        unordered_set<int>seen;
        for(int num: arr){
            int difference = target - num;
            if(seen.find(difference) != seen.end()){
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};