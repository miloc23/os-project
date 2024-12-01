import matplotlib.pyplot as plt
import numpy as np


inline_time = [2.4597958, 2.3980556, 1.3910165, 1.5001231, 3.5078919, 1.9247312]
noinline_time = [5.4260524, 3.7582888, 2.4439038, 2.6875191, 3.4189078, 3.0796997]
inline_error = [0.2419717542, 0.6679458759, 0.2368019603, 0.1413112034, 0.2272879178, 0.1095939184]
noinline_error = [0.4574551709, 1.114142318, 0.5001749441, 0.5727350562, 0.1864224147, 0.3034268315]

names = ["jiffies", "smp", "arg-cnt", "func-ip", "func-arg", "ret"]

x_axis = np.arange(6)

err_k=dict(ecolor='black', capsize=5, capthick=1)
plt.bar(x_axis - 0.2, inline_time, 0.4, label="INLINE", yerr=inline_error, error_kw=err_k)
plt.bar(x_axis + 0.2, noinline_time, 0.4, label="NOINLINE", yerr=noinline_error, error_kw=err_k)

plt.xticks(x_axis, names)

plt.xlabel("Helper Function")
plt.ylabel("Runtime (ns)")
plt.show()

