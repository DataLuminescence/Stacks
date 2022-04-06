import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class TestPuzzle {
    public static void main(String[] args) {
        

        PuzzleJava appTest = new PuzzleJava();

        appTest.getTenRolls(21, 1);
        System.out.print(appTest.getRandomLetter() + "\n");
        System.out.print(appTest.generatePassword(8) + "\n");
        appTest.generatePassword(4,8);
    }
}