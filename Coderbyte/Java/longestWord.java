// Solution to Longest Word Challenge using Java
//
// Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
// If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.

import java.util.Scanner;
import java.util.regex.*;

class Main {

  public static String LongestWord(String sen) {
    // delete all non-alphabet letters - if not a-zA-Z, replace with ''
    String temp = sen.replaceAll("[^a-zA-Z ]", "");
    String[] wordList = temp.split(" ");
    String longest = "";

    for (String word: wordList){
      if (word.length() > longest.length()){
        longest = word;
      }
    }

    return longest;
  }

  public static void main (String[] args) {
    System.out.print("Enter a sentence/string: ");
    Scanner s = new Scanner(System.in);
    String sen = s.nextLine();
    System.out.print("Longest word in '" + sen + "' is " + LongestWord(sen));
  }

}
