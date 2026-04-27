class Solution {
  public:
    int minDist(vector<int>& arr, int x, int y) {
        // code here
        int last_seen = -1;
        int minimum_distance = INT_MAX;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == x || arr[i] == y){
                if(last_seen != -1 && arr[i] != arr[last_seen]){
                    minimum_distance = min(minimum_distance, i - last_seen);
                }
                last_seen = i;
            }
        }
        return (minimum_distance == INT_MAX) ? -1 : minimum_distance;
    }
};