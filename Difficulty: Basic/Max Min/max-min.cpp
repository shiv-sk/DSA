// User function Template for C++

class Solution {
  public:
    int findSum(int A[], int N) {
        // code here.
        int maximum = INT_MIN;
        int minimum = INT_MAX;
        for(int i = 0; i<N; i++){
            if(A[i] < minimum){
                minimum = A[i];
            }
            if(A[i] > maximum){
                maximum = A[i];
            }
        }
        return minimum + maximum;
    }
};