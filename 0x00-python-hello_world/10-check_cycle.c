#include "lists.h"
/**
 * int check_cycle(listint_t *list) - checks the linkedlist if there are any cycles
 *
 * Return: 1 if there are cycles and 0 if there are none.
 */
int check_cycle(listint_t *list) {
  listint_t *initial;
  listint_t *current;

  initial = list;
  current = initial;
  while  (initial && initial->next && current && current->next)
  {
    if (current->n == initial->n) {
      return 1;
    }
    current = current->next;
  }
  return 0;
}


