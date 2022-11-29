#include "lists.h"
/**
 * int check_cycle(listint_t *list) - checks the linkedlist if there are any
 * cycles
 *
 * Return: 1 if there are cycles and 0 if there are none.
 */



int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *initial;
	initial = list;
	while(initial && current && current->next) {
		if(current->n == initial->n) {
			return (1);
		}
		current = current->next;
	}
	return (0);
}
