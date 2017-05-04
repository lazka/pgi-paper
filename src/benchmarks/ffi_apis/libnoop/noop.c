/*
 * Copyright 2015 Christoph Reiter
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 */

#include "noop.h"

void noop_void(void) {
}

double noop_double(double foo) {
    return foo;
}

size_t noop_str(char* foo) {
    return 42;
}
