#include "lists.h"
/**
 * insert_node - insert number in a sorted singly-linked list
 * @head: firstparmeter
 * @number:secondparemeter for the number to insert
 * Return: 0 if the function fails || pointer to the new node
 */
listint_t *insert_node(list_init **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t);
	if (new == NULL)
		return (NULL);
		new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
