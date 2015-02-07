#include<stdio.h>

struct node {
	int data;
	struct node *next;
};

void printList(struct node* n) {
	while(n != NULL) {
		printf("%d ", n->data);
		n = n->next;
	}
}

void push(struct node** head, int data) {
	struct node* temp = (struct node*) malloc(sizeof(struct node));
	temp->data = data;
	temp->next = (*head);
	(*head) = temp;	
}

void insertAfter(struct node* point, int data) {
	if (point == NULL) { 
      printf("the given previous node cannot be NULL");       
      return;  
    }
	struct node* temp = (struct node*) malloc(sizeof(struct node));
	temp->data = data;
	temp->next = point->next;
	point->next = temp;	
}

void append(struct node** head, int data) {
	struct node* temp = (struct node*) malloc(sizeof(struct node));
	struct node *last = *head;
	temp->data = data;
	temp->next = NULL;
	if((*head) == NULL) {
		(*head) = temp;
		return;
	}

	while(last->next != NULL) {
		last = last->next;
	}

	last->next = temp;
}

int main(void) {
	struct node* head = NULL;
	struct node* second = NULL;
	struct node* third = NULL;
	
	head = (struct node*) malloc(sizeof(struct node));
	second = (struct node*) malloc(sizeof(struct node));
	third = (struct node*) malloc(sizeof(struct node));

	head->data = 1;
	second->data = 2;
	third->data = 3;

	head->next = second;
	second->next = third;
	third->next = NULL;

	printList(head);
	printf("\n");
	push(&head, 0);
	printList(head);
	printf("\n");

	/* Start with the empty list */
  	struct node* headInsert = NULL; 
  
  	// Insert 6.  So linked list becomes 6->NULL
  	append(&headInsert, 6);
	 
  	// Insert 7 at the beginning. So linked list becomes 7->6->NULL
  	push(&headInsert, 7);
	 
  	// Insert 1 at the beginning. So linked list becomes 1->7->6->NULL
  	push(&headInsert, 1);
	 
  	// Insert 4 at the end. So linked list becomes 1->7->6->4->NULL
  	append(&headInsert, 4);
	 
  	// Insert 8, after 7. So linked list becomes 1->7->8->6->4->NULL
  	insertAfter(headInsert->next, 8);
	 
  	printf("\n Created Linked list is: ");
  	printList(headInsert);
	printf("\n");

	return 0;
}
