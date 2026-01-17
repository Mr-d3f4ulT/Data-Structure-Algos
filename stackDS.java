//Array Implementation of the Stack 

class StackUsingArray { 
    int top, capacity;
    int[] arr;
    //Constructor to initialize the stack
    public StackUsingArray(int capacity) {
      this.capacity = capacity;
      top = -1;
      arr = new int[capacity];
    }
    //Push function to insert elements in the stack
    public boolean push(int ele) {
      if(top >= capacity - 1) {
        System.out.println("Stack OverFlow");
        return false;
      }
      arr[++top] = ele; 
      return true;
    }
    //Pop Function to delete elements from the stack
    public int pop() {
      if(top < 0) {
        System.out.println("Stack UnderFlow");
        return 0;
      }
      return arr[top--];
    }
    //Peek Function to return the top-most element from the stack
    public int peek() {
      if(top < 0) {
        System.out.println("Stack Empty");
        return 0;
      }
      return arr[top];
    }
    //isEmpty function to check if stack is empty or not
    public boolean isEmpty() {
      return top < 0;
    }
}

//Linked List Implementation of the Stack 
class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
class StackUsingLinkedList {
    Node head;
    //Constructor to intialize the Stack
    StackUsingLinkedList() {
        this.head = null;
    }
    //To check if Stack is Empty or not 
    boolean isEmpty() {
        return head == null;
    }

    void pushEle(int ele) {
        Node newNode = new Node(ele);

        newNode.next = head;
        head = newNode;
    }

    void popEle() {
        if(isEmpty()) {
          System.out.println("Stack UnderFlow");
          return;
        }
        else {
          // Assign the current top to a temporary variable
          Node temp = head;

          // Update the top to the next node
          head = head.next;

          // Deallocate the memory of the old top node
          temp = null;

        }
    }
    int peek() {
        if(!isEmpty()) 
            return head.data;
        
        else {
            System.out.println("Stack is Empty");
            return Integer.MIN_VALUE;
        }
    }
}
public class stackDS {
  public static void main(String[] args) {
    StackUsingArray obj = new StackUsingArray(5);
    obj.push(1);
    obj.push(2);
    obj.push(3);
    obj.push(4);
    obj.push(5);

    System.out.println(obj.pop() + "  popped from Stack");
    
    System.out.println("Topmost Element of Stack is : " + obj.peek());
    
    System.out.println("Elements present in Stack are : ");

    while (!obj.isEmpty()) {
      System.out.print(obj.peek() + ", ");
      obj.pop();
    }
    
    StackUsingLinkedList obj1 = new StackUsingLinkedList();
    obj1.pushEle(10);
    obj1.pushEle(11);
    obj1.pushEle(12);
    obj1.pushEle(13);
    obj1.pushEle(14);
    obj1.pushEle(15);
    System.out.println();
    System.out.println();
    System.out.println("Top-Most Element of Stack is : " + obj1.peek());

    System.out.println("Elements present in Stack are : ");

    while (!obj1.isEmpty()) {
      System.out.print(obj1.peek() + ", ");
      obj1.popEle();
    }
  }
}