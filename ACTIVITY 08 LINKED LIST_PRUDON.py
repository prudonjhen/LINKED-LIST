class Node:
    """Represents a student in the queue (a node in the linked list)"""
    
    def __init__(self, name):
        self.name = name
        self.next_node = None


class StudentQueue:
    """Manages a queue of students using a singly linked list"""
    
    def __init__(self):
        self.head = None
    
    def add_student(self, name):
        """Add a student to the end of the queue"""
        new_node = Node(name)
        
        # If queue is empty, new student becomes the head
        if self.head is None:
            self.head = new_node
            return
        
        # Otherwise, traverse to the last node and attach the new node
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node
    
    def serve_student(self):
        """Remove and return the student at the front of the queue"""
        if self.head is None:
            print("The queue is empty. No student to serve.")
            return None
        
        served_student = self.head.name
        self.head = self.head.next_node
        return served_student
    
    def display_queue(self):
        """Display all student names in the queue"""
        if self.head is None:
            print("The queue is empty.")
            return
        
        students = []
        current = self.head
        while current is not None:
            students.append(current.name)
            current = current.next_node
        
        print("Students in queue: " + " -> ".join(students))
    
    def count_students(self):
        """Return the number of students currently in the queue"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count


# Demonstration of the Student Queue Management System
def main():
    queue = StudentQueue()
    
    # Initially, the queue is empty
    queue.display_queue()
    
    # Mia, Carlo, and Denise arrive
    queue.add_student("Mia")
    queue.add_student("Carlo")
    queue.add_student("Denise")
    queue.display_queue()
    
    # Serve the first student
    served = queue.serve_student()
    print(f"Now serving: {served}")
    
    # Ethan joins the line
    queue.add_student("Ethan")
    queue.display_queue()
    
    # Report the number of students waiting
    print(f"Number of students waiting: {queue.count_students()}")


if __name__ == "__main__":
    main()