#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * list: list checked
 * Return: 1 if cycle is detected and 0 if not
 */
int check_cycle(listint_t *list)
{

	listint_t *sl = list;
	listint_t *fs = list->next;

	if (list == NULL || list->next == NULL)
		return (0);

	while (sl != fs)
	{
		if (fs == NULL || fs->next == NULL)
			return (0);

		sl = sl->next;
		fs = fs->next->next;
	}

	return (1);
}
