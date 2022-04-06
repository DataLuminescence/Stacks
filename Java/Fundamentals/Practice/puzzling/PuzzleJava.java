import java.util.ArrayList;
import java.util.Random;

public class PuzzleJava{



    public int[] getTenRolls(int high, int low){
        int[] numArray;
        numArray = new int[10]; 

        Random randMachine = new Random();
        // randMachine.setSeed();

        for(int i=0; i < numArray.length; i++){
            numArray[i] = randMachine.nextInt(high-low) + low;
            System.out.print(numArray[i]);
        }





        return numArray;
    }


}