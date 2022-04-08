class Gorilla extends Mammal{
    
    // Constructor
    public Gorilla(){

    }

    public void throwSomething(int timesThrown){
        for(int i=0; i < timesThrown; i++){
            this.setEnergyLevel(getEnergyLevel() - 5);         
        }
        System.out.print("King Kong threw something "+ timesThrown + " times, which lowered it energy.\n");
        System.out.print("Energy level: " + displayEnergy() + "\n");
    }

    public void eatBananas(int timesEaten){
        for(int i=0; i < timesEaten; i++){
            this.setEnergyLevel(getEnergyLevel() + 10);        
        }
        System.out.print("King Kong is happy, because he ate " + timesEaten + " bananas, increasing energy.\n");
        System.out.print("Energy level: " + displayEnergy() + "\n");
    }

    public void climb(int timesClimbed){
        for(int i=0; i < timesClimbed; i++){
            this.setEnergyLevel(getEnergyLevel() - 10);      
        }
        System.out.print("King Kong climbed a tree "+ timesClimbed +" times, which lowered its energy.\n");
        System.out.print("Energy level: " + displayEnergy() + "\n");        
    }

}