#include <linux/bpf.h>
#include <linux/types.h>
#include <bpf/bpf_helpers.h>
#include "time-common.h"
#include "map.h"

char LISENSE[] SEC("license") = "Dual BSD/GPL";

/**
 * Counter program that traces the number of times this
 * hookpoint has been hit
 */
SEC("raw_tp")
int prog(void *ctx)
{
    // Once for caching
    //__u64 pid = bpf_get_current_pid_tgid();
    //__u64 jiffies = bpf_ktime_get_ns();
    //__u64 jiffies = bpf_jiffies64();
    struct map_test_val v;
    v.data[0] = 1;
    bpf_map_update_elem(&test_array_map, &first, &v, 0);
    // start the timer
    __u64 start = bpf_ktime_get_ns();
    // call helper in a tight loop
    for (int i = 0; i < ITERS; i++) {
        bpf_map_update_elem(&test_array_map, &first, &v, 0);
        //pid = bpf_get_current_pid_tgid();
        //jiffies = bpf_ktime_get_ns();
    }
    __u64 end = bpf_ktime_get_ns() - start;
    update_map(end);
    pr(jiffies, end);
    //bpf_printk("value was %lu\n", v->data[0]);
    //bpf_printk("PID: %lu. Took: %lu ns\n", jiffies, end);
    return 0;
}
