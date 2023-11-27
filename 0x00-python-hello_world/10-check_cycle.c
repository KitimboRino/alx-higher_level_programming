#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
listint_t *turtle = list;  /* Slow pointer */
listint_t *hare = list;    /* Fast pointer */

if (!list)
return (0);

while (turtle && hare && hare->next)
{
turtle = turtle->next;   /* Move the turtle one step */
hare = hare->next->next; /* Move the hare two steps */

if (turtle == hare)
return (1);  /* Cycle detected */
}

return (0);  /* No cycle found */
}
