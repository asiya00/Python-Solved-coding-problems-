public class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        Arrays.sort(arr);
        int min=arr[1]-arr[0];
        
        for(int i=1;i<arr.length-1;i++){
            if(arr[i+1]-arr[i]<min)
                min=arr[i+1]-arr[i];
        }
        
        for(int i=0;i<arr.length-1;i++){
            List<Integer> array = new ArrayList<Integer>();
            if(arr[i+1]-arr[i]==min){
                array.add(arr[i]);
                array.add(arr[i+1]);
            }
            if(array.size()>0)
                res.add(new ArrayList(array));
        }
        
        return res;
    }
    
}