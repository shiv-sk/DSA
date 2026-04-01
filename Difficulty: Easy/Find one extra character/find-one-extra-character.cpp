// User function Template for C++

char extraChar(string &s1, string &s2) {

    // code here
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    for(int i = 0; i < s2.size(); i++){
        if(s1[i] != s2[i]){
            return s2[i];
        }
    }
    return 'a';
}