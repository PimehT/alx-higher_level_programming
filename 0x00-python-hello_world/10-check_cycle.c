#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if the singly linked list has a cycle
 * @list: list to check
 *
 * Return: 0 if no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *step = list;
	listint_t *step_2 = list;

	while (step_2 != NULL && step_2->next != NULL)
	{
		step = step->next;
		step_2 = step_2->next->next;

		if (step == step_2)
			return (1);
	}

	return (0);
}
