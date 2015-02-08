import java.util.*;
import java.io.*;

	class Item implements Comparable<Item>{
		public double x, y;
		public String category;
    public double distance;
		public Item(double x, double y, String category) {
			this.x = x;
			this.y = y;
			this.category = category;
      this.distance = 0;
		}

    public int compareTo (Item item) {
      return (int) (Math.floor(this.distance - item.distance));  
    }

    public String toString() {
      return this.category + " " + this.x + " " + this.y +" " + this.distance + "\n";
    }

	}
public class hw1 {

	public static void main (String[] arg) {
  	ArrayList<Item> unclassified = new ArrayList<Item>();
    ArrayList<Item> classified = new ArrayList<Item>();
		Scanner scanner = new Scanner(System.in);
		System.out.println("Value of k");
		int k = scanner.nextInt();
		System.out.println("Value of M");
		int m = scanner.nextInt();
		System.out.println("Data file address");
		String filepath = scanner.next();
    System.out.println("Unclassified data");
		double x = 0;
		double y = 0;
		while ((x != 1.0) || (y != 1.0)) {
			x = scanner.nextDouble();
			y = scanner.nextDouble();
  	  Item item = new Item(x, y,  "");
			if ((x != 1.0) || (y != 1.0))unclassified.add(item);
		}
		//Reading the textfile
		try {
      Scanner fileScanner = new Scanner(new File(filepath));
			double xx, yy;
			String category;
			for (int i=0; i<m; i++) {
				category = fileScanner.next();
				xx = fileScanner.nextDouble();
				yy = fileScanner.nextDouble();
				Item item = new Item(xx, yy, category);
        classified.add(item);
			}
		}
		catch(Exception e){
      System.out.println("Bad filepath");
      System.exit(0);
		}

    //process inputs
    Item temp;
    for (Item unclass : unclassified) {
      String cat1 = "NOT_YET_DETERMINED";
      String cat2 = "NOT_YET_DETERMINED";
      int count1 = 1;
      int count2 = 0;
      ArrayList<Double> cat1Dist = new ArrayList<Double>();
      ArrayList<Double> cat2Dist = new ArrayList<Double>();
      String bestCat;
      System.out.printf("******** Processing Item (%f, %f) ********** \n", unclass.x, unclass.y);
      for (int i=0; i<m; i++) {
        temp = classified.get(i);
        temp.distance = distance(temp, unclass);
      }
      Collections.sort(classified);
      for (int i=0; i<k; i++) {
        temp = classified.get(i);
        //REQUIREMENT ONE
        System.out.println(temp);
        
        if (cat1.compareTo("NOT_YET_DETERMINED") == 0) {
          cat1 = temp.category;
          cat1Dist.add(temp.distance);
          }
        else {
            if (cat1.compareTo(temp.category) == 0) {
              count1 ++;
              cat1Dist.add(temp.distance);
            }
            else {
              cat2 = temp.category;
              count2 ++;
              cat2Dist.add(temp.distance);
            }
          }
        }
     
      bestCat = (count1 > count2)? cat1 : cat2;
      //REQUIREMET TWO
      System.out.printf("Data item (%f, %f) assigned to category %s \n", unclass.x, unclass.y, bestCat);  
      //System.out.println(classified);


      //REQUIREMENT THREE
      System.out.printf("Average distance to %s items: %f \n", cat1,  averageOfList(cat1Dist));
      System.out.printf("Average distance to %s items: %f \n", cat2,  averageOfList(cat2Dist));
      System.out.println();

    }

	}


  public static double averageOfList (List<Double> list) {
    double sum = 0;
    for (Double d : list) {
      sum += d;
    }
    return sum / list.size();
  }

	public static double distance (Item i, Item j) {
    return Math.sqrt(Math.pow((j.x - i.x),2) + Math.pow((j.y - i.y),2));
	}

}
