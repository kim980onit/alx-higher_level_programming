#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        second_half = slow->next;
    }
    else
    {
        second_half = slow;
    }

    prev_slow->next = NULL;
    reverse_list(&second_half);
    is_pal = compare_lists(*head, second_half);
    reverse_list(&second_half);

    if (fast != NULL)
    {
        prev_slow->next = slow;
        slow->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return (is_pal);
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 *
 * Return: 1 if the lists are the same, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
            return (0);
        head1 = head1->next;
        head2 = head2->next;
    }

    if (head1 == NULL && head2 == NULL)
        return (1);
    return (0);
}
