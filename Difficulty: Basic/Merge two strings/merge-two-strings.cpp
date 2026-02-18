
string merge(string S1, string S2) {
    // your code here
    string new_str = "";
    int index = 0;
    while(index < S1.size() && index < S2.size()){
        new_str += S1[index];
        new_str += S2[index];
        index++;
    }
    while(index < S1.size()){
        new_str += S1[index];
        index++;
    }
    while(index < S2.size()){
        new_str += S2[index];
        index++;
    }
    return new_str;
}