import java.util.ArrayList;

class TestHomework {
    public static void main(String[] args) {
        String testString = "BOND James bond";
        System.out.println(testString);
        System.out.println(listOfWords(testString).toString());
    
    //    OUTPUT:
    //    BOND James bond
    //    [BOND, James, bond]
    
    }
    
    public static ArrayList<String> listOfWords(String input) {
        ArrayList<String> output;
        String foundWord = "";
        int index = 0;
    
        // First advance past any starting spaces
        while (index < input.length() && input.charAt(index) == ' ') {
            index++;
        }
    
        // What if we are at the end of the string? Give an empty list and get out of here.
        if (index >= input.length())
            return new ArrayList<>();
    
        // Not done? White-space is gone so grab a word
        while (index < input.length() && input.charAt(index) != ' ') {
            foundWord = foundWord + input.charAt(index);
            index++;
        }
    
        // This return a recursive call of listOfWords, passing into it in the REST of
        // the string after our found word. Then add our found word to the START
        // of the list that is returned.
        output = listOfWords(input.substring(index));
        output.add(0, foundWord);
        return output;
    }
}