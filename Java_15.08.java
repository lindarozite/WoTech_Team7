//Cheese.java
package com.datorium.Datorium.API.DTOs;

public class Cheese {
    public String name;
}

//CheeseController.java
package com.datorium.Datorium.API.Controllers;

import com.datorium.Datorium.API.DTOs.Cheese;
import com.datorium.Datorium.API.DTOs.UpdateCheeseDTO;
import com.datorium.Datorium.API.Services.CheeseService;
import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;

@RestController
@RequestMapping("/cheese")

public class CheeseController {
    private CheeseService cheeseService;
    public CheeseController() {
        cheeseService = new CheeseService();
    }

    @PostMapping("/add")
    public int add(@RequestBody Cheese cheese){
        return cheeseService.add(cheese);
    }

    @GetMapping("/get")
    public ArrayList<Cheese> get(){
        return cheeseService.get();
    }

    @PostMapping("/update")
    public Cheese update(@RequestBody UpdateCheeseDTO updateCheeseDTO){
        return cheeseService.update(updateCheeseDTO.cheeseIndex, updateCheeseDTO.cheese);
    }
}

//CheeseService.java
package com.datorium.Datorium.API.Services;

import com.datorium.Datorium.API.DTOs.Cheese;
import com.datorium.Datorium.API.Repo.CheeseRepo;
import java.util.ArrayList;

public class CheeseService {
    private CheeseRepo cheeseRepo;

    public CheeseService(){
        cheeseRepo = new CheeseRepo();
    }

    public int add(Cheese cheese){
        return cheeseRepo.add(cheese);
    }
    public ArrayList<Cheese> get(){
        return cheeseRepo.get();
    }
    public Cheese update(int cheeseIndex, Cheese updateCheeseDTO){
        return cheeseRepo.update(cheeseIndex, updateCheeseDTO);
    }
}

//CheeseRepo.java
package com.datorium.Datorium.API.Repo;

import com.datorium.Datorium.API.DTOs.Cheese;
import java.util.ArrayList;

public class CheeseRepo {
    private ArrayList<Cheese> cheeseList = new ArrayList<>();

    public int add(Cheese cheese){
        cheeseList.add(cheese);
        return cheeseList.size();
    }

    public ArrayList get(){
        return cheeseList;
    }

    public Cheese update(int cheeseIndex, Cheese updateCheeseDTO){
        var cheese = cheeseList.get(cheeseIndex);
        cheese.name = updateCheeseDTO.name;
        return cheese;
    }
}

//UpdateCheeseDTO.java
package com.datorium.Datorium.API.DTOs;

public class UpdateCheeseDTO {
    public int cheeseIndex;
    public Cheese cheese;
}
