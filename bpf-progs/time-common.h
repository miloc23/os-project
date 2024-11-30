#define ITERS 1000

#define pr(name, time) bpf_printk(#name " took %lu\n", time); 
    
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 2);
    __type(key, __u32);
    __type(value, __u64);
} time_map SEC(".maps");

__u64 duration = 0;
__u64 count = 1;

__u64 read_dur;
// read duration

#define update_map(val) \
    void * dur = bpf_map_lookup_elem(&time_map, &duration); \
    if (! dur) return 0; \
    __u64 new_dur = *(__u64 *)dur + val; \
    bpf_map_update_elem(&time_map, &duration, &new_dur, 0); \
    void * cnt = bpf_map_lookup_elem(&time_map, &count); \
    if (! cnt) return 0; \
    __u64 new_cnt = *(__u64 *)cnt + ITERS; \
    bpf_map_update_elem(&time_map, &count, &new_cnt, 0); 
    
// update duration with new
// read count
// increment count
//



//define update_map(val) bpf_map_update_elem(&time_map, &key, val, 0);
