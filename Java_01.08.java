@PostMapping("/careerchange")
    public Career careerchange(@RequestBody Student student){
        var career = new Career();
        switch (student.name){
            case "Linda":
                career.profession = "Java Developer";
                break;
            case "Anita":
                career.profession = "Python Developer";
                break;
            case "Kristine":
                career.profession = "DevOps Engineer";
                break;
            case "Marta":
                career.profession = "Data Scientist";
                break;
            default:
                return null;
                //career.profession = "Unknown"; alternative return for default
            }
            return career;
        }


public class Career {
    public String profession;
}

public class Student {
    public String name;
}
