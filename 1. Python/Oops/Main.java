/*
 * This java file is created to clear the doubt of inheritance with respect to calling constructor.
 * Since in python, we need to call the constructor explicitly, I wanted to check whether the same goes with other languages or not
 * like java since i am familiar with it
 * Result: In java, When a class inherites the other class, implicitly java calls the default constructor of the parent calls if explicitly the constructor of parent is not called.
 * So, either we need to declare a default constructor with not calling the parent constructor using super(), in that case the values of attributes of parent constructor will set to its default values
 * or define a super key word with the number of attributes present in the parent class.
 * But in python, its not the case. We need to explicitly call the parent constructor.
 */

class Car {

    int windows;
    int doors;
    String engineType;

    public Car() {
        
    }
    public Car(int windows,int doors,String engineType) {

        this.windows = windows;
        this.doors = doors;
        this.engineType = engineType;
    }

    public String getEngineType() {
        return engineType;
    }

    public void setEngineType(String engineType) {
        this.engineType = engineType;
    }

    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }

    public int getWindows() {
        return windows;
    }

    public void setWindows(int windows) {
        this.windows = windows;
    }
}


class Tesla extends Car {

    boolean isSelfdriving;
    int price;

    public Tesla(boolean isSelfdriving,int price) {

        // super( windows, doors, engineType);
        this.isSelfdriving = isSelfdriving;
        this.price = price;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

}

public class Main{

    public static void main(String[] args) {

        // Scanner sc = new Scanner(System.in);
        Tesla car1 = new Tesla(true,123123);
        System.out.println(car1.isSelfdriving);
        System.out.println(car1.doors);
        System.out.println(car1.engineType);
    }
}