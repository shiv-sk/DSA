class Solution {
  public:
    vector<int> getThreeLargest(vector<int>& arr) {
        // code here
        int first = INT_MIN, second = INT_MIN, third = INT_MIN;
        vector<int>ans;
        for(int num: arr){
            if(num == first || num == second || num == third){
                continue;
            }
            if(num > first){
                third = second;
                second = first;
                first = num;
            }
            else if(num > second){
                third = second;
                second = num;
            }
            else if(num > third){
                third = num;
            }
        }
        if(first != INT_MIN)ans.push_back(first);
        if(second != INT_MIN)ans.push_back(second);
        if(third != INT_MIN)ans.push_back(third);
        return ans;
    }
};
