import java.util.ArrayList;

public class CafeUtil{

    public int getStreakGoal(int numWeeks){
        int sum = 0;
        for(int i=1; i <= numWeeks; i++){
            sum += i;
        }
        return sum;
    }

    public double getOrderTotal(double[] prices){
        double sum = 0;
        for(int i=0; i < prices.length; i++){
            sum += prices[i];
        }
        return sum;
    }

    
    public void displayMenu(ArrayList<String> menuItems){
        for(int i=0; i < menuItems.size(); i++){
            
            System.out.print("\n" + i + " " + menuItems.get(i) );

        }
        System.out.print("\n");
    }

    public boolean displayMenu(ArrayList<String> menuItems, ArrayList<Double> prices){
        if(menuItems.size() == prices.size()){
            
            for(int i=0; i < menuItems.size(); i++){
                System.out.format("%d - %s -- $%.2f\n", i, menuItems.get(i), prices.get(i));
            }
        System.out.print("\n");
        
        }else{
            return false;
        }

        return true;
    }

    public void addCustomer(ArrayList<String> customers){

        System.out.print("Please enter your name: ");
        String userName = System.console().readLine();
        System.out.print("Hello " + userName + "\n");

         // to add an item to an ArrayList
        System.out.print("There are " + customers.size() + " people in front of you");  
        customers.add(userName);      
    }

    public void printPriceChart(String product, double price, int maxQuantity){
        System.out.print("\n" + product + "\n");
        for(int i=1; i <= maxQuantity; i++){
            System.out.format("%d - $%.2f\n", i, price*i);
        }
        System.out.print("\n");

    }

    public void printPriceChart(String product, double price, int maxQuantity, double discount){
        System.out.print("\n" + product + "\n");
        for(int i=1; i <= maxQuantity; i++){
            System.out.format("%d - $%.2f\n", i, (price*i) - discount*(i-1) );
        }
        System.out.print("\n");

    }





}