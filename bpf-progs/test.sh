#!/usr/bin/bash
#

FILES="time-jiffies.kern.o time-smp.kern.o time-tracing-arg-cnt.kern.o time-tracing-func-ip.kern.o time-tracing-func.kern.o time-tracing-ret.kern.o"
TEST_RUN="time-jiffies.kern.o time-smp.kern.o" 
TRACING="time-tracing-arg-cnt.kern.o time-tracing-func-ip.kern.o time-tracing-func.kern.o time-tracing-ret.kern.o"

#FILES="time-jiffies.kern.o time-smp.kern.o time-tracing-arg-cnt.kern.o" 
for i in $TEST_RUN
do
    ./os-load.user $i prog
done

for i in $TRACING
do
    ./load.test.user $i prog
done

#./os-load.user time-jiffies.kern.o prog
#cat /sys/kernel/debug/tracing/trace > jiffies
#./os-load.user time-smp.kern.o prog
#cat /sys/kernel/debug/tracing/trace > smp
#./os-load.user time-func-arg-cnt.kern.o prog
#cat /sys/kernel/debug/tracing/trace > arg-cnt
#./os-load.user time-func-ip.kern.o prog
#cat /sys/kernel/debug/tracing/trace > func-ip
#./os-load.user time-func.kern.o prog
#cat /sys/kernel/debug/tracing/trace > func
#./os-load.user time-ret.kern.o prog
#cat /sys/kernel/debug/tracing/trace > ret
