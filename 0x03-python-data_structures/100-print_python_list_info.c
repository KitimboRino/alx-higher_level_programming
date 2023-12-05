#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t elem;

/* Print the size of the Python list */
printf("[*] Size of the Python List = %zd\n", Py_SIZE(p));

/* Print the allocated space for the Python list */
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

/* Loop through each element in the Python list and print its type */
for (elem = 0; elem < Py_SIZE(p); elem++)
printf("Element %zd: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}
