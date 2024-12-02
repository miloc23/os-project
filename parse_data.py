import sys
import numpy as np
import matplotlib.pyplot as plt

def parse_file(file):

    data = dict()
    
    for line in file:
        words = line.split(",")
        if len(words) > 2:
            print("Error")
            exit()
        key = words[0]
        val = int(words[1].rstrip())
        if key not in data:
            data[key] = list()
        data[key].append(val)
        #print(key, val)
    
    for k, v in data.items():
        avg = np.average(v) / 1000000
        stdev = np.std(v) /   1000000
        print(f"{k}: {avg} {stdev}")

    return data

if len(sys.argv) < 2:
    print("Failed: need to provide input file")
    exit()

file = open(sys.argv[1], "r")
inline = parse_file(file)
file.close()

file = open(sys.argv[2], "r")
noinline = parse_file(file)
file.close()

labels = list()
inline_time = list()
inline_error = list()
noinline_time = list()
noinline_error = list()

COUNT = 1000000 # 1 million

to_label = {"time-array-lookup.kern.o": "array_lookup",
            "time-array-update.kern.o": "array_update",
            "time-branch.kern.o": "snapshot_branch",
            "time-hash-lookup.kern.o": "hash_lookup",
            "time-hash-update.kern.o": "hash_update",
            "time-helper.kern.o": "helper",
            "time-jiffies.kern.o": "jiffies",
            "time-queue-peek.kern.o": "queue_peek",
            "time-queue-pop.kern.o": "queue_pop",
            "time-queue-push.kern.o": "queue_push",
            "time-smp.kern.o": "smp",
            "time-tracing-arg-cnt.kern.o": "arg_count",
            "time-tracing-func-ip.kern.o": "func_ip",
            "time-tracing-ret.kern.o": "func_ret",
            "time-tracing-func.kern.o": "func_arg",}

for key in inline.keys():
    if key in to_label.keys():
        labels.append(to_label[key])
    else:
        labels.append(key)
    inline_time.append(np.average(inline[key]) / COUNT)
    inline_error.append(np.std(inline[key]) / COUNT)
    noinline_time.append(np.average(noinline[key]) / COUNT)
    noinline_error.append(np.std(noinline[key]) / COUNT)



print(labels)
print(inline_time)
print(noinline_time)

x_axis = np.arange(len(labels))

err_k=dict(ecolor='black', capsize=5, capthick=1)
plt.bar(x_axis - 0.2, inline_time, 0.4, label="INLINE", yerr=inline_error, error_kw=err_k)
plt.bar(x_axis + 0.2, noinline_time, 0.4, label="NOINLINE", yerr=noinline_error, error_kw=err_k)

plt.xticks(x_axis, labels, rotation=90)
plt.xlabel("Helper Function")
plt.ylabel("Runtime (ns)")

plt.legend(loc="upper right")

plt.savefig("graph.png", bbox_inches="tight")

