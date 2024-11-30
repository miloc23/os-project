#include <linux/bpf.h>
#include <linux/types.h>
#include <bpf/bpf_helpers.h>
#include "time-common.h"

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
    __u32 id = bpf_get_smp_processor_id();
    //bpf_jiffies64();
    // start the timer
    __u64 start = bpf_ktime_get_ns();
    // call helper in a tight loop
    for (int i = 0; i < ITERS; i++) {
        //pid = bpf_get_current_pid_tgid();
        //jiffies = bpf_jiffies64();
        id = bpf_get_smp_processor_id();
    }
    __u64 end = bpf_ktime_get_ns() - start;
    //__u64 key = 0;
    update_map(end);
    //bpf_map_update_elem(&time_map, &key, &end, 0);
    pr(smp, end);
    //bpf_printk("PID: %lu. Took: %lu ns\n", id, end);
    return 0;
}
