import java.util.ArrayList;

public class TestOrders {
    public static void main(String[] args) {

        // Menu Items
        Item item1 = new Item();
        Item item2 = new Item();
        Item item3 = new Item();
        Item item4 = new Item();

        // Set Item Name
        item1.name = "Drip Coffee";
        item2.name = "Cappuccino";
        item3.name = "Latte";
        item4.name = "Mocha";

        // Set Item Price
        item1.price = 2.00;
        item2.price = 3.50;
        item3.price = 4.00;
        item4.price = 4.50;      

        // Order variables -- order1, order2 etc.
        Order order1 = new Order();
        Order order2 = new Order();
        Order order3 = new Order();
        Order order4 = new Order();

        // Set Order Name
        order1.name = "Cindhuri";
        order2.name = "Jimmy";
        order3.name = "Noah";
        order4.name = "Sam";

        // Create ArrayLists to be able to add items into them
        order1.items = new ArrayList<Item>();
        order2.items = new ArrayList<Item>();
        order3.items = new ArrayList<Item>();
        order4.items = new ArrayList<Item>();

        // Prints out Order@15db9742, which is an order type and the location of it in memory
        System.out.print(order1 + "\n");

        // It will not print anything as it has not been set? Wrong it prints out a default 0.0 
        System.out.printf("Total: %s\n", order1.total + "\n");


        // Add item1 to order2's item list and increment the order's total.
        order2.items.add(item1);
        order2.total += item1.price;
        System.out.printf("Name: %s\n", order2.name);

        for(int i=0; i < order2.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, order2.items.get(i).name, order2.items.get(i).price);
        }

        System.out.printf("Total: %s\n", order2.total);
        System.out.printf("Ready: %s\n", order2.ready + "\n");

        // ***************************************************************
        // Order.updateOrder(order2, item1);
        // ***************************************************************

        // order3 ordered a cappucino. Add the cappuccino to their order list and to their tab.
        order3.items.add(item2);
        order3.total += item2.price;
        System.out.printf("Name: %s\n", order3.name);

        for(int i=0; i < order3.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, order3.items.get(i).name, order3.items.get(i).price);
        }

        System.out.printf("Total: %s\n", order3.total);
        System.out.printf("Ready: %s\n", order3.ready + "\n");


        // order4 added a latte. Update accordingly.
        order4.items.add(item3);
        order4.total += item3.price;
        System.out.printf("Name: %s\n", order4.name);

        for(int i=0; i < order4.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, order4.items.get(i).name, order4.items.get(i).price);
        }
        System.out.printf("Total: %s\n", order4.total);
        System.out.printf("Ready: %s\n", order4.ready + "\n");


        // Cindhuri’s order is now ready. Update her status.
        order1.ready = true;
        System.out.printf("Name: %s\n", order1.name);

        for(int i=0; i < order1.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, order1.items.get(i).name, order1.items.get(i).price);
        }

        System.out.printf("Total: %s\n", order1.total);
        System.out.printf("Ready: %s\n", order1.ready + "\n");


        // Sam ordered more drinks - 2 lattes. Update their order as well.
        order4.items.add(item3);
        order4.total += item3.price;
        order4.items.add(item3);
        order4.total += item3.price;
        System.out.printf("Name: %s\n", order4.name);

        for(int i=0; i < order4.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, order4.items.get(i).name, order4.items.get(i).price);
        }
        System.out.printf("Total: %s\n", order4.total);
        System.out.printf("Ready: %s\n", order4.ready + "\n");

        // Jimmy’s order is now ready. Update his status.
        order2.ready = true;
        System.out.printf("Name: %s\n", order2.name);

        for(int i=0; i < order2.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, order2.items.get(i).name, order2.items.get(i).price);
        }

        System.out.printf("Total: %s\n", order2.total);
        System.out.printf("Ready: %s\n", order2.ready + "\n");
    }
}