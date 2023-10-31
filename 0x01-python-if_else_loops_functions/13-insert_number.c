#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to add to list
 *
 * Return: address of new nod or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *prev, *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);

	insert->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		insert->next = *head;
		*head = insert;
		return (insert);
	}

	current = *head;
	prev = NULL;
	while (current != NULL && number > current->n)
	{
		prev = current;
		current = current->next;
	}
	insert->next = current;
	prev->next = insert;

	return (insert);
}
