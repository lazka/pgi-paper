#include <Python.h>
#include <string.h>
#include <math.h>

#include <noop.h>

static PyObject* cwrapper_noop_str(PyObject* self, PyObject* args)
{
    char* raw_string;
    size_t out;

    if (!PyArg_ParseTuple(args, "s", &raw_string))
        return NULL;

    Py_BEGIN_ALLOW_THREADS;
    out = noop_str(raw_string);
    Py_END_ALLOW_THREADS;

    return PyInt_FromSize_t(out);
}

static PyObject* cwrapper_noop_double(PyObject* self, PyObject* args)
{
    double value;
    double out_value;

    if (!PyArg_ParseTuple(args, "d", &value))
        return NULL;

    Py_BEGIN_ALLOW_THREADS;
    out_value = noop_double(value);
    Py_END_ALLOW_THREADS;

    return PyFloat_FromDouble(out_value);
}

static PyObject* cwrapper_noop_void(PyObject* self) {
    Py_BEGIN_ALLOW_THREADS;
    noop_void();
    Py_END_ALLOW_THREADS;

    Py_RETURN_NONE;
}

static PyMethodDef ctest_funcs[] = {
    {"noop_str", (PyCFunction)cwrapper_noop_str, 
     METH_VARARGS, ""},
    {"noop_double", (PyCFunction)cwrapper_noop_double, 
     METH_VARARGS, ""},
    {"noop_void", (PyCFunction)cwrapper_noop_void, 
     METH_NOARGS, ""},
    {NULL}
};

void initcwrapper(void)
{
    Py_InitModule3("cwrapper", ctest_funcs, NULL);
}
