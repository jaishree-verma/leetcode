// 242
// optimal would be either use array or hashmap
// with array 
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        // array to store 26 letters of english alphabet
        int [] charCount = new int[26];
        // increment count for each character in s and decrement for each in t
        for(int i = 0;i<s.length();i++){
            charCount[s.charAt(i) - 'a']++;
            charCount[t.charAt(i) - 'a']--;
        }
        // check for non zero and return false
        for(int count: charCount){
            if(count != 0){
                return false;
            }
        }
        return true;

    }
}