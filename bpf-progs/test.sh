#!/usr/bin/bash
#

FILES="time-jiffies.kern.o time-smp.kern.o time-tracing-arg-cnt.kern.o time-tracing-func-ip.kern.o time-tracing-func.kern.o time-tracing-ret.kern.o time-array-lookup.kern.o time-array-update.kern.o time-hash-lookup.kern.o time-hash-update.kern.o"
TEST_RUN="time-jiffies.kern.o time-smp.kern.o time-array-lookup.kern.o time-array-update.kern.o time-hash-lookup.kern.o time-hash-update.kern.o time-queue-peek.kern.o time-queue-pop.kern.o time-queue-push.kern.o time-pid.kern.o"

TRACING="time-tracing-arg-cnt.kern.o time-tracing-func-ip.kern.o time-tracing-func.kern.o time-tracing-ret.kern.o"

#FILES="time-jiffies.kern.o time-smp.kern.o time-tracing-arg-cnt.kern.o" 
#

for t in $(seq $1)
do
    for i in $TEST_RUN
    do
        ./os-load.user $i prog
    done
    
    for i in $TRACING
    do
        ./load.test.user $i prog
    done
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
