class Solution {
    public int maxProfit(int[] prices) {

    int maxProfit = Integer.MIN_VALUE;
    if (prices == null || prices.length < 2) return 0;
        for (int i = 0; i < prices.length - 1; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                maxProfit = Math.max(maxProfit, prices[j] - prices[i]);
            }
        }
        return Math.max(maxProfit, 0);   
    } 
}







    // List<Integer> profits = new ArrayList<>();
    // int profit = 0;

    //     for(int i = 0; i < prices.length - 2; i++) {
    //         for(int j = 1; j < prices.length - 1; j++) {
    //             if(i > j) {
    //                 i++;
    //                 j++;
    //             } else {
    //             profit = prices[j] - prices[i];
    //             profits.add(profit);
    //             }
    //         }
    //     }
    //     (int out : prices) {
            
    //     }





            // if(i > j) {
            //     i++;
            //     j++;
            // }
            // if(prices[j] - prices[i] != NULL) {
                
            // }
