import java.util.Scanner;
import java.util.Random;

class BankAccount{
    
    //Class Attributes
    private double checkingBalance;
    private double savingsBalance;
    private long accountNum;
    private static int accounts = 0;
    private static int moneyStored = 0;

    // Constructor
    public BankAccount(){
        this.checkingBalance = 100;
        this.savingsBalance = 100;
        accountNum = randAccountNumber();
        this.accounts++;
    }

    // Overloaded Constructor
    public BankAccount(double checkingBalance, double savingsBalance){
        this.checkingBalance = 100;
        this.savingsBalance = 100;
        this.accounts++;
    }

    // Class methods ******************************************************************************************

    public void makeDeposit(double deposit){
        Scanner myAccount = new Scanner(System.in);
        System.out.println("Please select the account you would like to deposit into. Type 1 for checking, and 2 for savings.");
        String strAccount = myAccount.nextLine();
        int numAccount = Integer.parseInt(strAccount);

        if(numAccount == 1){
            setCheckingBalance(getCheckingBalance() + deposit);
            this.moneyStored += deposit;
            System.out.printf("You have deposited $%.2f into your checking account.", deposit);
        }else if(numAccount == 2){
            setSavingsBalance(getSavingsBalance() + deposit);
            this.moneyStored += deposit;
            System.out.printf("You have deposited $%.2f into your savings account.", deposit);
        }else{
            System.out.println("The selection you made is not valid. Exiting terminal.");
        }
    }

    public void makeWithdrawal(double withdrawal){
        
        Scanner myAccount = new Scanner(System.in);
        System.out.println("Please select the account you would like to withdraw from. Type 1 for checking, and 2 for savings.");
        String strAccount = myAccount.nextLine();
        int numAccount = Integer.parseInt(strAccount);
        
        if((withdrawal <= getCheckingBalance() && numAccount == 1) || (withdrawal <= getSavingsBalance() && numAccount == 2)){
            if(numAccount == 1){
                setCheckingBalance(getCheckingBalance() - withdrawal);
                this.moneyStored -= withdrawal;
                System.out.printf("You have withdrawn $%.2f from your checking account.", withdrawal);
            }else if(numAccount == 2){
                setSavingsBalance(getSavingsBalance() - withdrawal);
                this.moneyStored -= withdrawal;
                System.out.printf("You have withdrawn $%.2f from your savings account.", withdrawal);
            }else{
                System.out.println("The selection you made is not valid. Exiting terminal.");
            }
        }else{
            System.out.printf("You do not have sufficient funds to withdrawn $%.2f from your account.", withdrawal);
        }
    }

    public void totalMoney(){
        double total = getCheckingBalance() + getSavingsBalance();
        System.out.print("\nYour total money from both checking and savings is: " + total + "\n");
    }

    public long randAccountNumber(){
        int n = 10;
        long randAccount = (long) (Math.random()*Math.pow(10,10));
        setAccountNum(randAccount);
        return getAccountNum();
    }

    // Getters & setters ******************************************************************************************

    public void setCheckingBalance(double checkingBalance){
        this.checkingBalance = checkingBalance;
    }

    public void setSavingsBalance(double savingsBalance){
        this.savingsBalance = savingsBalance;
    }

    public void setAccountNum(long accountNum){
        this.accountNum = accountNum;
    }

    public double getCheckingBalance(){
        return checkingBalance;
    }

    public double getSavingsBalance(){
        return savingsBalance;
    }
    
    public long getAccountNum(){
        return accountNum;
    }

}


