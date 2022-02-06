   // Taking user input in Java
//        Scanner scan = new Scanner(System.in);
//        System.out.println("Enter Your Age");
//        int age = scan.nextInt();
//        System.out.println(input);

    // If-else conditionals
//        if(age>20){
//
//            System.out.println("You are an adult");
//        }
//        else if(age>5){
//            System.out.println("You are not a kid");
//
//        }
//        else{
//            System.out.println("You are a kid");
//        }
    //   Switch statement in Java

//        switch (age){
//            case 12:
//                System.out.println("You are 12 years old");
//                break;
//            case 56:
//                System.out.println("You are 56 years old");
//                break;
//            case 16:
//                System.out.println("You are 16 years old");
//                break;
//            default:
//                System.out.println("You did not match any of the cases");
//        }
    // Quick Quiz: print sunday to saturday based on numbers 1 to 7 typed by the user

        // Loops
        /*
        While Loop
        while(condition){
            // This code will keep executing until the condition is true
        }
         */
//        int i = 0;
//        while(i<100){
//            System.out.println(i);
//            i += 1;
//        }

        /*
        Do While Loop
        do{
            // This code will keep executing until the condition is true
        }while(condition)
         */
//        int j = 0;
//        do{
//            System.out.println(j);
//            j += 1;
//        }while(j>100);

        /*
        For Loop
        for(st1;st2;st3){
            //Code to be executed
            }
         */
//
//        for(int i=0;i<=10;i++){
//            if(i==2){
//                continue;
//            }
////            else{
////                System.out.println(i);
////            }
//            System.out.println(i);
//        }

    // Java Arrays
//        int [] marks = {1,2,3,5};
//        marks[3] = 34; // this will update marks[3]
//        System.out.println(marks[0]);
//        System.out.println(marks[3]);
//
//        // Classical way to iterate an array
//        for(int i=0;i<marks.length;i++){
//            System.out.println(marks[i]);
//        }
//        System.out.println("This is for each loop:");
//
//        // For each loop
//        for(int value:marks){
//            System.out.println(value);
//        }
//
//        int [][] matrix = {{1,2,3},
//                            {4,5,6}};
//        System.out.println(matrix[0][1]);
//
//        String [] cars = {"Maruti Harry", "Maruti", "Suzuki", "Innova", "Ford Titanium"};
//        for(String value:cars){
//            System.out.println(value);
//        }

        // Try - Catch
//        String [] cars = {"Maruti Harry", "Maruti", "Suzuki", "Innova", "Ford Titanium"};
//
//        try{
//            System.out.println(cars[3]);
//        }
//        catch(Exception e){
//            System.out.println(e);
//        }
//
//        System.out.println("Masoom");
//        System.out.println(sum(5, 7));

        float number_1, number_2;
        System.out.println("Enter first number");

        Scanner scan = new Scanner(System.in);
        number_1 = scan.nextFloat();

        System.out.println("Enter second number");
//        Scanner scan2 = new Scanner(System.in);
        number_2 = scan.nextFloat();
        System.out.print("You have Entered ");
        System.out.print(number_1);
        System.out.print(" and ");
        System.out.println(number_2);
        String prompt = "Enter 0 for addition, 1 for " +
                        "subtraction, 2 for multiplication and 3 for division";
        System.out.println(prompt);
        int input = scan.nextInt();
        switch (input){
            case 0:
                System.out.println("Adding these numbers");
                System.out.print("The result is: ");
                System.out.println(number_1 + number_2);
                break;

            case 1:
                System.out.println("Subtracting these numbers");
                System.out.print("The result is: ");
                System.out.println(number_1 - number_2);
                break;

            case 2:
                System.out.println("Multiplying these numbers");
                System.out.print("The result is: ");
                System.out.println(number_1 * number_2);
                break;

            case 3:
                System.out.println("Dividing these numbers");
                System.out.print("The result is: ");
                System.out.println(number_1 / number_2);
                break;

            default:
                System.out.println("Invalid input");

        }


    }
}

