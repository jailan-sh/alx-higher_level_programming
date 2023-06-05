#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function in C that checks if a singly linked
 * list has a cycle in it.
 * @list : head
 *
 * Return: 0 if no loop , 1 if loop presnts
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
