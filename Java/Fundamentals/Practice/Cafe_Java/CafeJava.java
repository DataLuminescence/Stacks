public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String notReadyMessage = ", your order is not ready. We appreciate your patience.";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double dripCoffeePrice = 2.0;
        double mochaPrice = 3.5;
        double lattePrice = 4.0;
        double cappuccinoPrice = 4.5;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = true;
        boolean isReadyOrder2 = false;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = false;
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)

        // Cindhuri

        System.out.println(String.format("%n" + generalGreeting + customer1 + pendingMessage + "."));
        System.out.println(String.format(customer1 + readyMessage + ". " + displayTotalMessage + dripCoffeePrice  + "."));

        
        // Noah

        System.out.println(String.format("%n" + generalGreeting + customer4 + "."));
        
        if(isReadyOrder2){
            System.out.println(String.format(customer4 + readyMessage + ". " + displayTotalMessage + cappuccinoPrice + "."));
        }
        else{
            System.out.println(String.format(customer4 + notReadyMessage + "."));
        }

        // Sam

        System.out.println(String.format("%n" + generalGreeting + customer2 + "."));
        System.out.println(String.format(customer2 + ", You ordered 2 lates. " + displayTotalMessage + (lattePrice * 2) + "."));
        
        if(isReadyOrder2){
            System.out.println(String.format(customer2 + readyMessage + "."));
        }
        else{
            System.out.println(String.format(customer2 + notReadyMessage + "."));
        }

        // Jimmy
        System.out.println(String.format("%n" + generalGreeting + customer3 + "."));
        System.out.println(String.format(displayTotalMessage + (lattePrice - dripCoffeePrice) + ".%n"));



    	// ** Your customer interaction print statements will go here ** //
    }
}
