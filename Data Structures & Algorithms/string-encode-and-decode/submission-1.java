class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for(String s : strs) {
            res.append(s.length()).append("!").append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        
        while (i < str.length()) {
            int j = i;
            // Find the position of the '#' delimiter
            while (str.charAt(j) != '!') {
                j++;
            }
            // Parse the length of the next string
            int length = Integer.parseInt(str.substring(i, j));
            // Extract the actual string and add it to the result list
            res.add(str.substring(j + 1, j + 1 + length));
            // Move the pointer to the start of the next encoded segment
            i = j + 1 + length;
        }
        
        return res;
    }
}