#include "lists.h"
/**
 * int check_cycle(listint_t *list) - checks the linkedlist if there are any
 * cycles
 *
 * Return: 1 if there are cycles and 0 if there are none.
 */
int check_cycle(listint_t *list)
{
	listint_t *next;
	listint_t *prev;

	next = list;
	prev = list;
	while (list && next && next->next)
	{
		list = list->next;
		next = list->next;
		if (list == next)
		{
			list = prev;
			prev =  next;
			while (1)
			{
				next = prev;
				while (next->next != list && next->next != prev)
				{
					next = next->next;
				}
				if (next->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
