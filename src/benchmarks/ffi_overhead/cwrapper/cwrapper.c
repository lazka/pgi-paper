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

#include <Python.h>
#include <string.h>
#include <math.h>

#include <overhead.h>

static PyObject* cwrapper_overhead(PyObject* self, PyObject* args)
{
    PyObject* list = NULL, *text = NULL, *conv = NULL;
    int32_t *array = NULL;
    char *string;
    int status;
    size_t len;
    int err;

    if (!PyArg_ParseTuple (args, "OO", &list, &text))
        return NULL;

    if (text == Py_None) {
        string = NULL;
    } else {
        if (!PyString_Check (text)) {
            if (PyUnicode_Check (text)) {
                conv = PyUnicode_AsEncodedString (text, "utf-8", "strict");
                if (conv == NULL) {
                    goto error;
                }
                string = PyString_AsString (conv);
            } else {
                PyErr_SetString (PyExc_TypeError, "not a list");
                goto error;
            }
        } else {
            string = PyString_AsString (text);
        }
    }

    if (!PyList_Check (list)) {
        PyErr_SetString (PyExc_TypeError, "not a list");
        goto error;
    }

    len = PyList_GET_SIZE (list);
    array = PyMem_New (int32_t, len);
    if (list == NULL) {
        PyErr_SetNone (PyExc_MemoryError);
        goto error;
    }

    for (size_t i=0; i < len; i++)
    {
        PyObject* item = PyList_GET_ITEM (list, i);
        PyObject* num = PyNumber_Int (item);
        long l;
        if (num == NULL) {
            goto error;
        }
        l = PyInt_AsLong (num);
        Py_DECREF (num);
        if (l == -1 && PyErr_Occurred())
            goto error;
        if (l < INT32_MIN || l > INT32_MAX) {
            PyErr_SetString (PyExc_OverflowError, "overflow");
            goto error;
        }
        array[i] = (int32_t)l;
    }

    Py_BEGIN_ALLOW_THREADS;
    status = overhead (array, len, string, &err);
    Py_END_ALLOW_THREADS;

    PyMem_Del (array);
    Py_XDECREF (conv);

    if (!status) {
        PyErr_SetString (PyExc_Exception, "error occured");
        return NULL;
    }

    return PyInt_FromLong (status);
error:
    Py_XDECREF (conv);
    PyMem_Del (array);
    return NULL;
}

static PyMethodDef ctest_funcs[] = {
    {"overhead", (PyCFunction)cwrapper_overhead,
     METH_VARARGS, ""},
    {NULL}
};

void initcwrapper(void)
{
    Py_InitModule3("cwrapper", ctest_funcs, NULL);
}
