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

#labels = list()
#inline_time = list()
#inline_error = list()
#noinline_time = list()
#noinline_error = list()

items = 14
labels = [""] * items 
inline_time = [0] * items
inline_error = [0] * items
noinline_time = [0] * items
noinline_error = [0] * items
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
            "time-tracing-func.kern.o": "func_arg",
            "time-pid.kern.o": "pid", }

to_index = {"time-array-lookup.kern.o": 6,
            "time-array-update.kern.o": 7,
            "time-branch.kern.o": 15,
            "time-hash-lookup.kern.o": 8,
            "time-hash-update.kern.o": 9,
            "time-helper.kern.o": 16,
            "time-jiffies.kern.o": 0, 
            "time-queue-peek.kern.o": 10,
            "time-queue-pop.kern.o": 11,
            "time-queue-push.kern.o": 12,
            "time-smp.kern.o": 1,
            "time-tracing-arg-cnt.kern.o": 2,
            "time-tracing-func-ip.kern.o": 3,
            "time-tracing-ret.kern.o": 4, 
            "time-tracing-func.kern.o": 5,
            "time-pid.kern.o": 13, }

for key in inline.keys():
    #if key != "time-pid.kern.o":
    print(key, to_index[key])
    if key in to_label.keys():
        labels[to_index[key]] = to_label[key]
    #else:
        #labels.append(key)
    inline_time[to_index[key]] = np.average(inline[key]) / COUNT
    inline_error[to_index[key]] = np.std(inline[key]) / COUNT
    noinline_time[to_index[key]] = np.average(noinline[key]) / COUNT
    noinline_error[to_index[key]] = np.std(noinline[key]) / COUNT



print(labels)
#print(inline_time)
#print(noinline_time)

exp_inline_time = inline_time[0:13]
exp_inline_error = inline_error[0:13]

exp_noinline_time = noinline_time[0:13]
exp_noinline_error = noinline_error[0:13]
exp_labels = labels[0:13]
print(exp_labels)
x_axis = np.arange(len(exp_labels))

err_k=dict(ecolor='black', capsize=5, capthick=1)
plt.bar(x_axis - 0.2, exp_inline_time, 0.4, label="INLINE", yerr=exp_inline_error, error_kw=err_k)
plt.bar(x_axis + 0.2, exp_noinline_time, 0.4, label="NOINLINE", yerr=exp_noinline_error, error_kw=err_k)

plt.xticks(x_axis, exp_labels, rotation=90)
plt.xlabel("Helper Function")
plt.ylabel("Runtime (ns)")

plt.legend(loc="upper right")

#plt.savefig("graph.png", bbox_inches="tight", dpi=500)

# make pid plot
plt.clf()

plt.bar([0,1], [inline_time[13], noinline_time[13]], yerr=[inline_error[13], noinline_error[13]], error_kw=err_k)
plt.xticks([0,1], ["our pid inline", "original"])
plt.xlabel("PID Inlined")
plt.ylabel("Runtime (ns)")

#plt.savefig("pid.png", bbox_inches="tight", dpi=500)

print(noinline_time[13] - inline_time[13])
