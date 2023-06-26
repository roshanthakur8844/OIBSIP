//Roshan Kishor Thakur


import java.util.Scanner;

public class ATMInterface {
    private static Scanner scanner = new Scanner(System.in);
    private static double balance = 1000.0; // Initial balance

    public static void main(String[] args) {
        boolean quit = false;

        while (!quit) {
            System.out.println("ATM Interface");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Quit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character

            switch (choice) {
                case 1:
                    checkBalance();
                    break;
                case 2:
                    deposit();
                    break;
                case 3:
                    withdraw();
                    break;
                case 4:
                    quit = true;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }

            System.out.println();
        }
    }

    private static void checkBalance() {
        System.out.println("Your balance is: $" + balance);
    }

    private static void deposit() {
        System.out.print("Enter the amount to deposit: $");
        double amount = scanner.nextDouble();
        scanner.nextLine(); // Consume the newline character

        if (amount > 0) {
            balance += amount;
            System.out.println("Deposit of $" + amount + " successful.");
        } else {
            System.out.println("Invalid amount. Please try again.");
        }
    }

    private static void withdraw() {
        System.out.print("Enter the amount to withdraw: $");
        double amount = scanner.nextDouble();
        scanner.nextLine(); // Consume the newline character

        if (amount > 0) {
            if (amount <= balance) {
                balance -= amount;
                System.out.println("Withdrawal of $" + amount + " successful.");
            } else {
                System.out.println("Insufficient balance. Please try again.");
            }
        } else {
            System.out.println("Invalid amount. Please try again.");
        }
    }
}