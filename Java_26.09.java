package com.datorium.Datorium.API.CityLottery;

import java.util.List;
import java.util.Random;

public class CityService {

    private ICityRepository cityRepository;

    public CityService(ICityRepository cityRepository){
        this.cityRepository = cityRepository;
    }

    public City getRandomCity() throws Exception {
        var cities = cityRepository.getCities();

        int totalPopulation = calculateTotalPopulation(cities);
        int randomValue = getRandomValue(totalPopulation);

        return findCityByLotteryTicket(cities, randomValue);
    }

    private int calculateTotalPopulation(List<City> cities) {
        // 1. Count total amount of citizens
        int totalPopulation = 0;
        for (City city : cities) {
            totalPopulation += city.getPopulation();
        }
        return totalPopulation;
    }

    private int getRandomValue(int totalPopulation) {
        // 2. Choose random number based on the total population
        Random random = new Random();
        return random.nextInt(totalPopulation);
    }

    private City findCityByLotteryTicket(List<City> cities, int randomValue) throws Exception {
        // 3. Loop through cities to find the city based on the lottery ticket logic
        for (City city : cities) {
            randomValue -= city.getPopulation();
            if (randomValue <= 0) {
                return city;
            }
        }
        throw new Exception("Something went wrong, city not found.");
    }
}
