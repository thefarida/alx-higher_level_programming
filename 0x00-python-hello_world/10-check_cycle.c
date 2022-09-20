#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list contains a cycle
 * @list: The singly linked list to be checked
 *
 * Return: 1 if cycle is present, 0 if it is not.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
