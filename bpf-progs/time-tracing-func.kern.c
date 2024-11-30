#include <linux/bpf.h>
#include <linux/types.h>
#include <bpf/bpf_helpers.h>
#include "time-common.h"

char LISENSE[] SEC("license") = "Dual BSD/GPL";

/**
 * Counter program that traces the number of times this
 * hookpoint has been hit
 */
SEC("fentry/ksys_read")
int prog(void *ctx)
{
    // Once for caching
    //__u64 pid = bpf_get_current_pid_tgid();
    __u64 val;
    __u64 jiffies = bpf_get_func_arg(ctx, 0, &val);
    //bpf_jiffies64();
    // start the timer
    __u64 start = bpf_ktime_get_ns();
    // call helper in a tight loop
    for (int i = 0; i < ITERS; i++) {
        //pid = bpf_get_current_pid_tgid();
        //jiffies = bpf_jiffies64();
        jiffies = bpf_get_func_arg(ctx, 0, &val);
    }
    __u64 end = bpf_ktime_get_ns() - start;
    bpf_printk("val %lu\n", jiffies);
    update_map(end);
    pr(func_arg, end);
    //bpf_printk("func_arg PID: %lu. Took: %lu ns\n", jiffies, end);
    return 0;
}
