import java.util.ArrayList;

public class TestAccounts {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount();
        BankAccount account2 = new BankAccount();

        account1.makeDeposit(300);
        account1.makeWithdrawal(500);
        account1.totalMoney();
    }
}
