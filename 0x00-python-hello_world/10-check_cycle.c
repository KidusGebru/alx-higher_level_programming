#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 If there is no cycle, 1 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *fut1, *fut2;

	if (list == NULL || list->next == NULL)
		return (0);

	fut1 = list->next;
	fut2 = list->next->next;

	while (fut1 && fut2 && fut2->next)
	{
		if (fut1 == fut2)
			return (1);

		fut1 = fut1->next;
		fut2 = fut2->next->next;
	}

	return (0);
}
