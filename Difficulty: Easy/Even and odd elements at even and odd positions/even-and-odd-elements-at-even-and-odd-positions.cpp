class Solution {

  public:
    vector<int> arrangeOddAndEven(vector<int>& arr) {
        // Your code goes here
        vector<int> evens, odds;
        for(int num: arr){
            if(num % 2 == 0) evens.push_back(num);
            else odds.push_back(num); 
        }
        int i = 0, e = 0, o = 0;
        vector<int> ans(arr.size());
        while(i < arr.size()){
            if(i % 2 == 0 && e < evens.size()){
                ans[i] = evens[e++];
            }
            else if(i % 2 == 1 && o < odds.size()){
                ans[i] = odds[o++];
            }else{
                break;
            }
            i++;
        }
        while (e < evens.size()){
            ans[i++] = evens[e++];
        }
        while (o < odds.size()){
            ans[i++] = odds[o++];
        }
        return ans;
    }
};
