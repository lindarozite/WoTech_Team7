//MathService class
package com.datorium.Datorium.API;

public class MathService {

    public int sum(int a, int b){
        if(a+b > 100){
            return 0;
        }
        else{
            return a+b;
        }
    }
}


//MathService test
package com.datorium.Datorium.API;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class MathServiceTest {

    MathService mathService = new MathService();

    @Test
    public void testSumBelow100() {
        assertEquals(50, mathService.sum(10, 40), "Sum of 20 and 30 is 50");
    }

    @Test
    public void testSumExactly100() {
        assertEquals(100, mathService.sum(50, 50), "Sum of 50 and 50 is 100");
    }

    @Test
    public void testSumAbove100() {
        assertEquals(0, mathService.sum(70, 50), "Sum of 70 and 50 should be 0 because it exceeds 100");
    }
}
