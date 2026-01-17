class Node {
  int data;
  Node next;
  // Constructor to initialize the node with data
  public Node(int data) { 
    this.data = data;
    this.next = null;
  }
}

class singlyLinkedList {
  
  Node head; //created head node
  
  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 TRAVERSAL or DISPLAY or PRINTING IN SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  public void traversalList(Node head) {
    // ✅ Time Complexity: O(n), where n is the number of nodes in the linked list.
    // ✅ Auxiliary Space: O(1)
    while(head != null) {
      System.out.print(head.data + " -> ");
      head = head.next;
    }
    System.out.println("NULL");
  }
  
  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥  INSERTION IN SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  // 📌Insertion at Beginning
  public void insertionAtBeginning(int data) {
    Node newNode = new Node(data);
    newNode.next = head;
    head = newNode;
  }
  
  // 📌Insertion at End
  public void insertionAtEnd(int data) {
    Node newNode = new Node(data);
    
    if(head == null) {
      head = newNode;
      return;
    }
    
    Node temp = head;
    
    while(temp.next != null) {
      temp = temp.next;
    }
    temp.next = newNode;
  }
  
  // 📌Insertion at Any Position
  public void insertionAtAnyPosition(int data, int position) {
    Node newNode = new Node(data);

    if(position == 1) {
      newNode.next = head;
      head = newNode;
      return;
    }
    
    Node temp = head; //temp pointed to head
    
    for(int i = 1; i < position - 1 && temp.next != null; i++)  {  // Traverse to the node that will be present just before the new node
      temp = temp.next;
    }
    
    if (temp == null) return; // if position of temp is greater than number of elements
    
    newNode.next = temp.next; // update the next pointers
    temp.next = newNode;
  }
  
  // 📌Insertion before any value
  public void insertionByValue(int data, int nodeVal) {
    Node newNode = new Node(data);
    if(head == null) {
      head = newNode;
      return;
    }
    if(head.data == nodeVal) {
      newNode.next = head;
      head = newNode;
      return;
    }

    Node prev = null;
    Node current = head;

    while (current != null) {
        if (current.data == nodeVal) {
            newNode.next = current;
            if (prev != null) {
                prev.next = newNode;
            }
            return;
        }
        prev = current;
        current = current.next;
    }
  }

  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 DELETION IN SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  // 📌Deletion at Beginning 
  public void deletionAtBeginning() {
    
    if(head == null) return; //Check if the list is empty 
    head = head.next; //Move head to next of head.
  }
  
  // 📌Deletion at End 
  public void deletionAtEnd() {
    
    if(head == null) return; //Check if the list is empty 
    if(head.next == null) {
      head = null;
      return;
    }
    Node temp = head;
    while (temp.next.next != null) { //move the temp to second Last node
        temp = temp.next;
    }

    temp.next = null; //then remove last node
  }
  
  // 📌Deletion at Specific Position 
  public void deletionByPosition(int position) {
    
    if(head == null || position < 1) return; //Check if the list is empty or if the position is valid or not 
    
    if(position == 1) {
      head = head.next;
      return;
    }
    Node temp = head; 
    for(int i = 1; i < (position - 1) && temp.next != null; i++) { //traverse to node at just before the specific position node we want to delete
      temp = temp.next;
    }
    if(temp == null || temp.next == null) return; //Check if the position is out of range or next node is null, meaning there's nothing to delete)

    temp.next = temp.next.next; //move the temp.next to node adjacent to node we want to delete.
  }
  
  // 📌Deletion by Value
  public void deletionByValue(int deleteData) {
    
    if(head == null) return; //Check if the list is empty 
    
    if(head.data == deleteData) {
      head = head.next;
      return;
    }

    Node temp = head; 
    while(temp.next.data != deleteData && temp.next != null) { //traverse to node at just before the specific node with the value u want to delete
      temp = temp.next;
    }
    if(temp.next == null) return; //If value not found

    temp.next = temp.next.next; //move the temp.next to node adjacent to node we want to delete.
  }

  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 SEARCHING IN SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  public boolean searchingList(Node head, int target) {
    // ✅ Time Complexity: O(n), where n is the number of nodes in the linked list.
    // ✅ Auxiliary Space: O(1)
    Node currNode = head;
    while (currNode != null) {
      if (currNode.data == target)
        return true;
        currNode = currNode.next;
    }
    return false;
  }
  
  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 LENGTH OF SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  public int lengthOfList(Node head) {
    // ✅ Time Complexity: O(n), where n is the number of nodes in the linked list.
    // ✅ Auxiliary Space: O(1)
    int length = 0;
    while(head != null) {
      head = head.next;
      length++;
    }
    return length;
  }

  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 REVERSE A SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  public void reverseList(Node head) {
    Node prev = null;
    Node curr = head;
    //Traverse the list
    while(curr != null) {
      Node nextNode = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nextNode;
    }
    head = prev;
    traversalList(head);
  }
  
  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 FINDING MIDDLE OF A SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  public void middleOfList(Node head) {
    
  }

  //🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔥 SORTING SINGLY LINKED LIST 🔥🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
  public void sortList(Node head) {
    
  }
}
public class linkedList {
  public static void main(String[] args) {

    singlyLinkedList sll = new singlyLinkedList();
    /*
      The sll.head that your methods are actually modifying was never initialized with your nodes. That’s why deletionByPosition() doesn’t affect the list you're printing — it's operating on null.
      if you dont want to manually assign head then do this 
      sll.insertionAtEnd(10);
      sll.insertionAtEnd(20);
      sll.insertionAtEnd(30);
      sll.insertionAtEnd(40);
      sll.traversalList(sll.head); // use the actual object’s head
      sll.deletionByPosition(2);
      sll.traversalList(sll.head);

      remove the manual assigning of head, sll.head = head and remove 
      Node head = new Node(10);
      head.next = new Node(20);
      head.next.next = new Node(30);
      head.next.next.next = new Node(40);
    */
    Node head = new Node(1);
    head.next = new Node(2);
    head.next.next = new Node(3);
    head.next.next.next = new Node(4);
    
    sll.head = head; //<- 👈 this is the key, for manual assigning of head
    
    sll.traversalList(sll.head); 

    sll.insertionAtBeginning(5);
    sll.insertionAtEnd(6);
    sll.insertionAtAnyPosition(7, 6);
    sll.traversalList(sll.head); 

    // sll.deletionByPosition(4);
    // sll.traversalList(sll.head);

    sll.deletionByValue(4);
    sll.traversalList(sll.head);
    //System.out.println(sll.searchingList(sll.head, 10));
    //System.out.println(sll.lengthOfList(sll.head));
    sll.reverseList(sll.head);
  }
}
