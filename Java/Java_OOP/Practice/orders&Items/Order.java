import java.util.ArrayList;

public class Order{
    public String name;
    public double total;
    public boolean ready;
    public ArrayList<Item> items;
}

// public void updateOrder(Order order, Item item){
    
//     order.items.add(item);
//     order.total += item.price;
//     System.out.print(order.total + "\n");

// }