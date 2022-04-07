import java.util.ArrayList;

public class TestOrders {
    public static void main(String[] args) {
        
        // Menu Items
        Item item1 = new Item("Drip Coffee", 2.00);
        Item item2 = new Item();
        Item item3 = new Item();
        Item item4 = new Item();

        // Set Item Name

        item2.setName("Cappuccino");
        item3.setName("Latte");
        item4.setName("Mocha");

        // Set Item Name

        item2.setPrice(3.50);
        item3.setPrice(4.00);
        item4.setPrice(4.50);

        // Create orders with constructor
        Order order1 = new Order();
        Order order2 = new Order();

        // Create orders with overloaded constructor
        Order order3 = new Order("Cindhuri");
        Order order4 = new Order("Jimmy");
        Order order5 = new Order("Noah");

        // Add items to orders
        order1.addItem(item1);
        order1.addItem(item2);
        
        order2.addItem(item2);
        order2.addItem(item3);
        
        order3.addItem(item3);
        order3.addItem(item4);

        order4.addItem(item4);
        order4.addItem(item1);

        order5.addItem(item4);
        order5.addItem(item2);

        // Get status of a specific order
        order3.setReady(true); //For testing
        System.out.print(order3.getStatusMessage() + "\n");

        order4.setReady(false); //For testing
        System.out.print(order4.getStatusMessage() + "\n");

        // Print out the total for a specific order
        System.out.println(order1.getOrderTotal());

        // Display all order details 
        order3.display();

    }
}
