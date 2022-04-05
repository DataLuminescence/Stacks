public class AlfredTest {
    /*
    * This main method will always be the launch point for a Java application
    * For now, we are using the main to test all our 
    * AlfredQuotes methods.
    */
    public static void main(String[] args) {
        // Make an instance of AlfredQuotes to access all its methods.
        AlfredQuotes alfredBot = new AlfredQuotes();
        
        // Make some test greetings, providing any necessary data
        String testGreeting = alfredBot.basicGreeting();
        String testGuestGreeting1 = alfredBot.guestGreeting();
        String testGuestGreeting2 = alfredBot.guestGreeting("Beth Kane");
        String testGuestGreeting3 = alfredBot.guestGreeting("Master Bruce", "Morning");

        String testDateAnnouncement = alfredBot.dateAnnouncement();
        
        String alexisTest = alfredBot.respondBeforeAlexis(
                            "Alexis! Play some low-fi beats."
                            );
        String alfredTest = alfredBot.respondBeforeAlexis(
            "I can't find my yo-yo. Maybe Alfred will know where it is.");
        String notRelevantTest = alfredBot.respondBeforeAlexis(
            "Maybe that's what Batman is about. Not winning. But failing.."
        );
        
        // Print the greetings to test.
        System.out.println(String.format("%n" + testGreeting));
        
        // Uncomment these one at a time as you implement each method.
        System.out.println(String.format("%n" + testGuestGreeting1));
        System.out.println(String.format("%n" + testGuestGreeting2));
        System.out.println(String.format("%n" + testGuestGreeting3));                
        System.out.println(String.format("%n" + testDateAnnouncement));
        System.out.println(String.format("%n" + alexisTest));
        System.out.println(String.format("%n" + alfredTest));
        System.out.println(String.format("%n" + notRelevantTest));
    }
}
