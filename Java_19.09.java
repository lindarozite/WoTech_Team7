//NumberGame.java

public class NumberGame {

    public int guessNumber(int n) {
        int number = 12;
        if(n > number){
            return 3;
        }
        else if(n < number){
            return 2;
        }
        return 1;
    }
}

//NumberGameTest

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class NumberGameTest {

    @Test
    public void testCorrectGuess() {
        NumberGame game = new NumberGame();
        int result = game.guessNumber(12); // Hardcoded correct number is 12
        assertEquals(1, result, "Guessing the correct number should return 1");
    }

    @Test
    public void testTooLowGuess() {
        NumberGame game = new NumberGame();
        int result = game.guessNumber(5);  // Any number < 12 should return 2
        assertEquals(2, result, "Guessing a number lower than 12 should return 2");
    }

    @Test
    public void testTooHighGuess() {
        NumberGame game = new NumberGame();
        int result = game.guessNumber(20); // Any number > 12 should return 3
        assertEquals(3, result, "Guessing a number higher than 12 should return 3");
    }
}

