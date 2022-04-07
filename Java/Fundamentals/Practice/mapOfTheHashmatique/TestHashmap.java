import java.util.HashMap;
import java.util.Set;

public class TestHashmap {
    public static void main(String[] args) {

        HashMap<String, String> trackList = new HashMap<String, String>();

        trackList.put("Portions for Foxes", "Rilo Kiley");
        trackList.put("Sunrise Sunset", "Bright Eyes");
        trackList.put("Paranoiattack", "The Faint");
        trackList.put("The Recluse", "Cursive");
        trackList.remove("Paranoiattack");

        Set<String> keys = trackList.keySet();
        for(String key : keys) {
            System.out.println(key + ": " + trackList.get(key));  
        }
    }
}