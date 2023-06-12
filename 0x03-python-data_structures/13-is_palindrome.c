#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : pointer to first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current = NULL;
	listint_t *temp = *head;

	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == NULL)
			slow = slow->next;
		else if (fast->next == NULL)
			slow = slow->next->next;
	}
	current = slow;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	while (temp && prev)
	{
		if ((temp)->n != prev->n)
			return (0);
		temp = temp->next;
		prev = prev->next;
	}

	return (1);
}
