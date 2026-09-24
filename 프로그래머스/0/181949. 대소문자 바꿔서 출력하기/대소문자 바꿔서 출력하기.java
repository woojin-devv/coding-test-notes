import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Solution {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
        String a = sc.next();
        List<Character> list = new ArrayList<>();
        String result = "";

        for (char c : a.toCharArray()) {
            list.add(c);
        }

        for (char c : list) {
            char ch;
            if (Character.isUpperCase(c)) {
                ch = Character.toLowerCase(c);
            } else {
                ch = Character.toUpperCase(c);
            }
            result += ch;
        }
        System.out.println(result);
    }
}