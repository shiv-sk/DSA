

class Solution {
  public:
    string calc_Sum(vector<int>& arr1, vector<int>& arr2) {
        // Complete the function
        int i = arr1.size()-1;
        int j = arr2.size()-1;
        string final_sum = "";
        int carry = 0;
        
        while(i >= 0 || j >= 0 || carry){
            int sum = carry;
            
            if(i >= 0){
                sum += arr1[i];
                i--;
            }
            if(j >= 0){
                sum += arr2[j];
                j--;
            }
            
            final_sum.push_back((sum % 10) + '0');
            carry = sum / 10;
        }
        reverse(final_sum.begin(), final_sum.end());
        return final_sum;
    }
};