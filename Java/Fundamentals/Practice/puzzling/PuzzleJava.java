import java.util.ArrayList;
import java.util.Random;

public class PuzzleJava{

    public int[] getTenRolls(int high, int low){
        int[] numArray;
        numArray = new int[10]; 
        Random randMachine = new Random();

        for(int i=0; i < numArray.length; i++){
            numArray[i] = randMachine.nextInt(high-low) + low;
            System.out.print(numArray[i] + "\n");
        }
        return numArray;
    }

    public String getRandomLetter(){
        String[] letterArray = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};

        Random randMachine = new Random();
        

        return letterArray[randMachine.nextInt(26-1) + 1];
    }     
    
    public String generatePassword(int passLength){
        String randPassword = "";
        for(int i=0; i < passLength; i++){
            randPassword += getRandomLetter();
        }
        return randPassword;
    }

    public String[] generatePassword(int listLength, int passLength){
        String[] randPassList;
        randPassList = new String[listLength]; 


        for(int i=0; i < listLength-1; i++){
            String randPassword = "";
            for(int j=0; j < passLength; j++){
                randPassword += getRandomLetter();
            }
            randPassList[i] = randPassword;
            System.out.print(randPassword + "\n");
        }

        return randPassList;
    }

    // What kind of array does it take any type of array?
    // public void shuffleArray(ArrayList<T> someArray = new ArrayList<T>()){

    // }

}