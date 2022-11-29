#include "lists.h"
#include <stddef.h>
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node, *current_node;

  new_node = *head;
  current_node = new_node;

  if(new_node == NULL)
  {
    return (NULL);
  }

  while(current_node && current_node->next && current_node->n < number && current_node->next->n < number){
    current_node = current_node-> next;
  }

  new_node = current_node;


  return new_node;
}
