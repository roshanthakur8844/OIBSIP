//Roshan Kishor Thakur


import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    public static void main(String[] args) {
        int maxNumber = 100;
        int randomNumber = generateRandomNumber(maxNumber);
        int attempts = 0;
        boolean hasWon = false;

        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("I've picked a number between 1 and " + maxNumber + ".");
        System.out.println("Can you guess it?");

        Scanner scanner = new Scanner(System.in);

        while (!hasWon) {
            System.out.print("Enter your guess: ");
            int guess = scanner.nextInt();
            attempts++;

            if (guess == randomNumber) {
                hasWon = true;
                System.out.println("Congratulations! You guessed the number in " + attempts + " attempts.");
            } else if (guess < randomNumber) {
                System.out.println("Too low! Try again.");
            } else {
                System.out.println("Too high! Try again.");
            }
        }

        scanner.close();
    }

    private static int generateRandomNumber(int maxNumber) {
        Random random = new Random();
        return random.nextInt(maxNumber) + 1;
    }
}