class Solution {
  public:
    // Function to count the number of digits in n that evenly divide n
    int evenlyDivides(int n) {
        // code here
        int number = n;
        int count = 0;
        while(number){
            int digit = number%10;
            if(digit > 0 && (n%digit) == 0){
                count++;
            }
            number/=10;
        }
        return count;
    }
};