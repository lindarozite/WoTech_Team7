//1.Create an array in the endpoint, fill the array with data and access it from the URL

//version1
@GetMapping("/array")
    public String[] getArray(){
        String[] arrayTeam =  {"Anita", "Kristine", "Linda", "Marta"};
        return arrayTeam;
    }

//version2
@GetMapping("/colors")
    public String[] colors() {
        String[] colors = {"Blue", "Green", "Yellow", "Orange"};
        return colors;
    }

//2.Create an object (new class, cheese or wine or whatever) in the endpoint, fill the object, access it from the URL

//House.java

package com.datorium.Datorium.API;

public class House {
    private String address;
    private int floors;
    private int year;

    public House(String address, int floors, int year) {
        this.address = address;
        this.floors = floors;
        this.year = year;
    }
    public String getAddress() {
        return address;
    }

    public int getFloors() {
        return floors;
    }

    public int getYear() {
        return year;
    }
}

//Main.java
package com.datorium.Datorium.API;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
@CrossOrigin
public class DatoriumApiApplication {

    public static void main(String[] args) {
        System.out.println("asd");
        SpringApplication.run(DatoriumApiApplication.class, args);
    }

    @GetMapping("/ping")
    public String ping() {
        return "pong";
    }

    @GetMapping("/hello")
    public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
        return String.format("Hello %s!", name);
    }
    @GetMapping("/sum")
    public int sum(@RequestParam(value = "num1") int num1, @RequestParam(value = "num2") int num2) {
        return num1 + num2;
    }
    @GetMapping("/colors")
    public String[] colors() {
        String[] colors = {"Blue", "Green", "Yellow", "Orange"};
        return colors;
    }
    @GetMapping("/house")
    public House house(@RequestParam(value = "address") String address,
                       @RequestParam(value = "floors") int floors,
                       @RequestParam(value = "year") int year) {
        House house = new House(address, floors, year);
        return house;
    }
}

//Query
http://localhost:8080/house?address=Brivibas&floors=2&year=2005
