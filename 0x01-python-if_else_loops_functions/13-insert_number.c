#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
/* Declare pointers for the current node and the new node */
listint_t *node = *head, *new;

/* Allocate memory for the new node */
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

/* Set the value of the new node to the given number */
new->n = number;

/* If the list is empty or the new node should be inserted at the beginning */
if (node == NULL || node->n >= number)
{
new->next = node;
*head = new;
return (new);
}

/* Traverse the list to find the correct position for the new node */
while (node && node->next && node->next->n < number)
node = node->next;

/* Insert the new node into the list */
new->next = node->next;
node->next = new;

/* Return a pointer to the new node */
return (new);
}
