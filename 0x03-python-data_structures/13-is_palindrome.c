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
	int size = 0;
	int i, j;
	listint_t *ptr = *head;

	if (ptr == NULL)
		return (0);

	while (ptr != NULL)
	{
		arr = (int *)realloc(arr, size * sizeof(int));
		if (arr == NULL)
			exit(1);

		arr[size] = ptr->n;
		size++;
		ptr = ptr->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		for (j = size - 1; j <= i; j--)
		{
			if (arr[i] != arr[j])
			{
				free(arr);
				return (0);
			}
		}
	}
	free(arr);
	return (1);
}
