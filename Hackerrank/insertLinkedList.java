/*
Solution in Java for Day 15: Linked List in 30 Days of Coding on Hackerrank.

Complete the insert function so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the  parameter. Once the new node is added, return the reference to the  node.

Note: If the  argument passed to the insert function is null, then the initial list is empty.

Sample Input
The first line contains T, the number of test cases.
The  subsequent lines of test cases each contain an integer to be inserted at the list's tail.

4
2
3
4
1

Sample Output
2 3 4 1

Explanation
T=4, so we will be inserting 4 nodes.
The list is initially empty, so head is null; accounting for this, our code returns a new node containing the data value 2 as the data of our list. We then create and insert nodes 3, 4, and 1 at the tail of our list. The resulting list returned by the last call to  is , so the printed output is 2 3 4 1.

*/

import java.io.*;
import java.util.*;

class Node {
	int data;
	Node next;
	Node(int d) {
        data = d;
        next = null;
    }
}

class Solution {

    public static  Node insert(Node head,int data) {
        //Complete this method
				
				//Node newNode = new Node(data); //would not work since the recursion step will create this new node every call, creating extra nodes/duplicates
        //check if linkedlist is empty
        if (head == null){
            //if true return the new node
            return new Node(data);
        }

        //check if head points to null (if it is the last node in the linkedlist)
        if(head.next == null){
            //if true, point to the new node
            head.next = new Node(data);
        }
        //if false, traverse through the linkedlist until the tail node
        else{
            insert(head.next, data);
        }
        return head; //return the linkedlist
    }

	public static void display(Node head) {
        Node start = head;
        while(start != null) {
            System.out.print(start.data + " ");
            start = start.next;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Node head = null;
        int N = sc.nextInt();

        while(N-- > 0) {
            int ele = sc.nextInt();
            head = insert(head,ele);
        }
        display(head);
        sc.close();
    }
}
