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
	printList(second);
	printf("\n");
	printList(third);
	return 0;
}
