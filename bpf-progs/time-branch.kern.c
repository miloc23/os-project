#include <linux/bpf.h>
#include <linux/types.h>
#include <linux/perf_event.h>
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
    //__u64 jiffies = bpf_ktime_get_ns();
    struct perf_branch_entry pbe;
    long res = bpf_get_branch_snapshot(&pbe, sizeof(struct perf_branch_entry), 0);
    if (res < 0) {
        bpf_printk("Error %ld\n", res);
    }
    
    //__u64 jiffies = bpf_jiffies64();
    //// start the timer
    //__u64 start = bpf_ktime_get_ns();
    //// call helper in a tight loop
    //for (int i = 0; i < ITERS; i++) {
    //    //pid = bpf_get_current_pid_tgid();
    //    jiffies = bpf_jiffies64();
    //    //jiffies = bpf_ktime_get_ns();
    //}
    //__u64 end = bpf_ktime_get_ns() - start;
    //update_map(end);
    //pr(jiffies, end);
    //bpf_printk("PID: %lu. Took: %lu ns\n", jiffies, end);
    return 0;
}
