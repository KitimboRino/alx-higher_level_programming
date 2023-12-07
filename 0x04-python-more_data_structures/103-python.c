#include <Python.h>

/**
 * print_python_list - Print information about a Python list.
 * @p: PyObject representing the Python list.
 */
void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
fprintf(stderr, "Invalid Python List Object\n");
return;
}

Py_ssize_t size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);

printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (Py_ssize_t i = 0; i < size; ++i)
{
PyObject *item = PyList_GetItem(p, i);
const char *type = Py_TYPE(item)->tp_name;
printf("Element %ld: %s\n", i, type);
}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: PyObject representing the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
if (!PyBytes_Check(p))
{
fprintf(stderr, "Invalid Python Bytes Object\n");
return;
}

printf("[.] bytes object info\n");
printf("  size: %ld\n", PyBytes_Size(p));

/* Print a maximum of 10 bytes */
printf("  trying string: %s\n", PyBytes_AsString(p));

printf("  first %ld bytes: ", PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10);

for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i)
{
printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
if (i < 9)
printf(" ");
}

printf("\n");
}
