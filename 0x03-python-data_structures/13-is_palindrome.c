#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

listint_t *reverse_list(listint_t *head);
/**
 * reverse_list: reverses a linked list
 * @head: pointer to head node parameter
 * Return: New reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0 if not palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if ((*head) == NULL || (*head)->next == NULL)
		return 1;

	/* Moving slow pointer by 1 step and fast pointer by two */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = reverse_list(slow);

	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
			return (0);
		(*head) = (*head)->next;
		slow = slow->next;
	}

	return (1);
}
