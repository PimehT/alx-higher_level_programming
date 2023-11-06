#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node
 *
 * Return: 1 if palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *second_half = NULL;
	listint_t *prev = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	prev = NULL;
	second_half = slow;
	while (second_half)
	{
		listint_t *next = second_half->next;

		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}

	second_half = prev;
	while (second_half)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	return (is_palindrome);
}

