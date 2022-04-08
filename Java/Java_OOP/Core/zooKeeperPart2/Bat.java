class Bat extends Mammal{
    
    // Constructor
    public Bat(int energyLevel){
        this.setEnergyLevel(energyLevel);
    }

    public void fly(int timesFlown){
        for(int i=0; i < timesFlown; i++){
            this.setEnergyLevel(getEnergyLevel() - 50);
        }
        System.out.print("Whoosh! CountChocula Flew "+ timesFlown +" times, which lowered their energy.\n");
        System.out.print("Energy level: " + displayEnergy() + "\n");
    }

    public void eatHumans(int humansEaten){
        for(int i=0; i < humansEaten; i++){
            this.setEnergyLevel(getEnergyLevel() + 25);
        }
        System.out.print("CountChocula is happy, because he ate " + humansEaten + " humans, increasing energy.\n");
        System.out.print("Energy level: " + displayEnergy() + "\n");
    }

    public void attackTown(int townsAttacked){
        for(int i=0; i < townsAttacked; i++){
            this.setEnergyLevel(getEnergyLevel() - 100);
        }
        System.out.print("CountChocula attacked "+ townsAttacked + " towns, which lowered their energy.\n");
        System.out.print("Energy level: " + displayEnergy() + "\n");
    }
}