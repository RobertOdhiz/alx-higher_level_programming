#include "lists.h"
/**
 * insert_node - inserts a node
 * @head: pointer to head pointer
 * @number: data for inserted node
 * Return: memory address of inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *prev = NULL;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = curr;
	}

	return (new_node);
}
