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
	int *arr = NULL;
	int size = 0, half;
	int i, j;
	listint_t *ptr = *head;

	if (ptr == NULL)
		return (0);

	while (ptr != NULL)
	{
		arr = (int *)realloc(arr, (size + 1) * sizeof(int));
		if (arr == NULL)
			exit(1);

		arr[size] = ptr->n;
		size++;
		ptr = ptr->next;
	}

	half = size / 2;
	for (i = 0; i < half; i++)
	{
		for (j = size - 1; j <= i; j--)
		{
			if (arr[i] == arr[j])
				continue;
			else
				return (0);
		}
	}
	return (1);
}
