/* Copyright 2016 Christoph Reiter <reiter.christoph@gmail.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library. If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdlib.h>
#include <Python.h>
#include <noop.h>
#include <limits.h>


static PyObject* cwrapper_int_list_args(PyObject* self, PyObject* args)
{
    PyObject *obj;
    Py_ssize_t i, len, val;
    int *list;

    if (!PyArg_ParseTuple(args, "O", &obj))
        return NULL;

    len = PySequence_Length (obj);
    if (len == -1)
        return NULL;

    list = PyMem_New(int, len);
    if (list == NULL)
        return PyErr_NoMemory();

    PyErr_Clear();
    for (i = 0; i < len; ++i) {
        PyObject* item = PySequence_Fast_GET_ITEM (obj, i);
        val = PyInt_AsSsize_t(item);
        if (val == -1 && PyErr_Occurred())
            goto error;
        if (val < INT_MIN || val > INT_MAX) {
            PyErr_SetString(PyExc_OverflowError, "overflow");
            goto error;
        }
        list[i] = val;
    }

    Py_BEGIN_ALLOW_THREADS;
    int_list_args(list);
    Py_END_ALLOW_THREADS;

    PyMem_Del(list);
    Py_RETURN_NONE;
error:
    PyMem_Del(list);
    return NULL;
}

static PyMethodDef ctest_funcs[] = {
    {"int_list_args", (PyCFunction)cwrapper_int_list_args, 
     METH_VARARGS, ""},
    {NULL}
};

void initcwrapper(void)
{
    Py_InitModule3("cwrapper", ctest_funcs, NULL);
}
