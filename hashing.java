import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
// 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 HASH MAP 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
class hashmapdemo {
  /* 
    🛠️ Key Features of HashMap
    ✅ Stores key-value pairs (<K, V>)
    ✅ Allows null values and one null key
    ✅ Unordered (No guarantee of element order)
    ✅ Fast operations – O(1) average time complexity
    ✅ Uses hashing internally (hashCode())
    ✅ Not thread-safe (Use ConcurrentHashMap for multithreading)
  */

  //🛠️Creating a hashmap
  HashMap<Integer, String> hmap = new HashMap<>();
  {
    //🔹Adding Key - Value pair, the curly braces as used as Instance initializer block cause the HashMap is created outside a method
    //put(K key, V value) → Adds a key-value pair to the HashMap.
    hmap.put(1, "Shivansh Pandey");
    hmap.put(2, "Suryansh Vikaram Singh");
    hmap.put(3, "Hitesh Chandra");
    hmap.put(4, "Jitendra Bhatwadekar");

    //🔹Printing whole HashMap
    System.out.println(hmap); 
    System.out.println();

    //🔹Acessing values of HashMap
    //get(K key) → Returns the value associated with the key. If the key doesn’t exist, it returns null.
    System.out.println(hmap.get(1));
    System.out.println(hmap.get(2));
    System.out.println();

    //🔹Removing elements
    //remove(K key) → Removes the key-value pair from the map.
    hmap.remove(1);
    System.out.println(hmap);
    System.out.println();

    //🔹Iterating Hash Map
    //using forEach()
    hmap.forEach((key, value) -> System.out.println(key + " -> " + value));
    System.out.println();
    
    //🔹Getting Only keys or values
    //using keySet() and values()
    //System.out.println(hmap.keySet());   
    System.out.println(hmap.values());  
    System.out.println();

    //containsKey(K)	Checks if a key exists
    //containsValue(V)	Checks if a value exists
    //size()	Returns the number of entries

    // ✅✅✅ USING HASHMAP TO COUNT FREQUENCY OF ELEMENTS IN ARRAY 
    int[] arr = {1, 2, 3, 2, 5, 3};

    HashMap<Integer, Integer> frequencyMap = new HashMap<>();
    HashMap<Integer, Integer> frequencyMap1 = new HashMap<>();

    for (int i = 0; i < arr.length; i++) {
        frequencyMap.put(arr[i], frequencyMap.getOrDefault(arr[i], 0) + 1);
    }
    System.out.println(frequencyMap);

    // We can either use getOrDefault() to count frequency or we can use containsKey() method to count

    for (int i = 0; i < arr.length; i++) {
      if (frequencyMap1.containsKey(arr[i])) {
        frequencyMap1.put(arr[i], frequencyMap1.get(arr[i]) + 1);
      } else {
        frequencyMap1.put(arr[i], 1);
      }
    }
    System.out.println(frequencyMap1);

  }
}

// 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 HASH SET 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
class hashsetdemo {
  HashSet<Integer> hset = new HashSet<>(); {
    //Adding elements
    hset.add(10);
    hset.add(20);
    hset.add(30);
    hset.add(40);
    hset.add(50);
    //Printing whole HashSet
    System.out.println(hset);
    //Remove elements
    hset.remove(10);
    System.out.println(hset);

    //Check if and element exists
    System.out.println(hset.contains(10)); //Returns false for this example

    //Check size 
    System.out.println(hset.size());

    //clear() to clear all elements
    //isEmpty() to check if hash set is empty or not

    //Iterating HashSet
    Iterator<Integer> it = hset.iterator();
    while (it.hasNext()) {
      System.out.println(it.next());
    }
  }
}
public class hashing {
  public static void main(String[] args) {
    System.out.println("HASHMAP");
    System.out.println();
    //hashmapdemo map = new hashmapdemo();
    System.out.println();
    System.out.println("HASHSET");
    System.out.println();
    //hashsetdemo set = new hashsetdemo();
  }
}
