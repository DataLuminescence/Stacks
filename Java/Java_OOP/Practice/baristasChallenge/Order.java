import java.util.ArrayList;

class Order{

    // Member Variable
    private String name;
    private boolean ready;
    private ArrayList<Item> items;
    
    // Constructor
    public Order(){
        this.name = "guest";
        this.items = new ArrayList<Item>();
    }

    // Overloaded Constructor
    public Order(String name){
        this.name = name;
        this.items = new ArrayList<Item>();
    }   

    // ******************************************************************************************

    public void addItem(Item item){
        this.items.add(item);
    }

    public String getStatusMessage(){
        if(this.getReady()){
            return "\n"+ this.getName() + ", your order is ready.";
        }else{
            return "\n"+ this.getName() + ". Thank you for waiting. Your order will be ready soon.";
        }
    }

    public double getOrderTotal(){
        double sum = 0;
        for(int i=0; i < this.items.size(); i++){
            sum += this.items.get(i).getPrice();
        }
        return sum;
    }

    public void display(){
        System.out.printf("\nName: %s\n", this.name);

        for(int i=0; i < this.items.size(); i++){
            System.out.printf("Item: %d - %s - $%.2f\n", i+1, this.items.get(i).getName(), this.items.get(i).getPrice());
        }

        System.out.printf("Total: $%.2f\n", this.getOrderTotal());
        System.out.print(this.getStatusMessage() + "\n");
    }

    // ******************************************************************************************

    public void setName(String name){
        this.name = name;
    }

    public void setReady(boolean ready){
        this.ready = ready;
    }

    public void setItems(ArrayList<Item> items){
        this.items = items;
    }

    public String getName(){
        return name;
    }

    public boolean getReady(){
        return ready;
    }

    public ArrayList<Item> getItems(){
        return this.items;
    }

}