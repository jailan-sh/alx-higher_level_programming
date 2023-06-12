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

	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	current = slow;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	while (*head && prev)
	{
		if ((*head)->n != prev->n)
			return (0);
		*head = (*head)->next;
		prev = prev->next;
	}

	return (1);
}
