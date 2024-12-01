/**
 * User program for loading a single generic program and attaching
 * Usage: ./load.user bpf_file bpf_prog_name
 */
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <time.h>
#include <stdlib.h>

#include <bpf/bpf.h>
#include <bpf/libbpf.h>

int main(int argc, char *argv[])
{
    if (argc != 3) {
        printf("Not enough args\n");
        printf("Expected: ./load.user bpf_file bpf_prog_name\n");
        return -1;
    }

    char * bpf_path = argv[1];
    char * prog_name = argv[2];

    // Open the shared1.kern object
    struct bpf_object * prog = bpf_object__open(bpf_path);
    
    // Try and load this program
    // This should make the map we need
    if (bpf_object__load(prog)) {
        printf("Failed");
        return 0;
    }

    struct bpf_program * program = bpf_object__find_program_by_name(prog, prog_name);

    if (program == NULL) {
        printf("Shared 1 failed\n");
        return 0;
    }

    int prog_fd = bpf_program__fd(program);

    __u64 arg = 128;


    struct bpf_test_run_opts opts;
    opts.sz = sizeof(struct bpf_test_run_opts);
    opts.ctx_in = (void *)&arg;
    opts.ctx_size_in = 8;
    opts.batch_size = 0;
    opts.cpu = 0;

    for (int i = 0; i < 1000; i++) {
        bpf_prog_test_run_opts(prog_fd, &opts);
    }

    struct bpf_map * my_map = bpf_object__find_map_by_name(prog, "time_map");
    if (!my_map) {
        printf("failed to get map\n");
        return 0;
    }

    __u64 dur_key = 0;
    __u64 cnt_key = 1;
    __u64 duration = 0;
    __u64 count = 0;
    bpf_map__lookup_elem(my_map, &dur_key, 4, &duration, 8, 0);
    bpf_map__lookup_elem(my_map, &cnt_key, 4, &count, 8, 0);
    //printf("path: %s duration was %llu with count %llu\n", bpf_path, duration, count);
    printf("%s, %llu\n", bpf_path, duration);
    //printf("Duration was: %u\n", opts.duration);

    return 0;
}


