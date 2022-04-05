import java.util.Date;
import java.text.SimpleDateFormat;

public class AlfredQuotes {
    
    public String basicGreeting() {
        // You do not need to code here, this is an example method
        return "Hello, lovely to see you. How are you?";
    }

    public String guestGreeting(String name) {
        return "Hello, " + name + ". Top of the morning to you.";
    }
    
    public String dateAnnouncement() {
        Date date = new Date();
        return "It is currently " + date;
    }
    
    public String respondBeforeAlexis(String conversation) {
        if(conversation.indexOf("Alexis") != -1){
            return "Right away, sir. We must not let Bezos become a super hero as well.";
        }else if(conversation.indexOf("Alfred") != -1){
            return "I am sworn to carry your burden.";
        }else{
            return "Right. And with that I shall retire.";
        }
    }
    
	// NINJA BONUS
	// See the specs to overload the guessGreeting method
    public String guestGreeting(String name, String dayPeriod) {
        return "Good " + dayPeriod + ", " + name + ". Who will you beat within an inch of their life today?";
    }
    // SENSEI BONUS
    // Write your own AlfredQuote method using any of the String methods you have learned!
    public String guestGreeting() {

        SimpleDateFormat dayPeriod = new SimpleDateFormat("HH");
        Date date = new Date();
        int hour = Integer.parseInt((dayPeriod.format(date)));

        if(hour >= 0 && hour < 12){
            return "Good morning Master Wayne. Any broken ribs from last night?";
        }else if(hour >= 12 && hour < 6){
            return "Good afternoon Master Wayne. Shall I prepare the batsuit?";
        }else if(hour >= 6 && hour < 9){
            return "Good evening Master Wayne. Will you be joining me for dinner?";
        }else if(hour >= 9 && hour < 0){
            return "Good night Master Wayne. Lets hope that man wakes up from that coma you put him in.";
        }
        return "Error";
    }
}


