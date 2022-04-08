
class Mammal{

    // Member Variable
    private int energyLevel;
    
    // Constructor
    public Mammal(){
        this.energyLevel = 100;
    }

    // Overloaded Constructor
    public Mammal(int energyLevel){
        this.energyLevel = 100;
    }   

    // ******************************************************************************************

    public int displayEnergy (){
        return this.getEnergyLevel();
    }

    // ******************************************************************************************

    public void setEnergyLevel(int energyLevel){
        this.energyLevel = energyLevel;
    }

    public int getEnergyLevel(){
        return energyLevel;
    }

}