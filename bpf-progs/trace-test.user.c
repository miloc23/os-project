#include <stdio.h>
#include <unistd.h>

void main() {
    char buf[256];
    for (int i = 0; i < 1000000; i++)
        read(0, buf, 0);
}
