#!/usr/bin/python3
from bcc import BPF
import time

# Define the eBPF program in C
bpf_text = """
#include <uapi/linux/ptrace.h>

struct key_t {
    char comm[16];
};

BPF_HASH(opens, struct key_t);

int count_opens(struct pt_regs *ctx) {
    struct key_t key = {};
    bpf_get_current_comm(&key.comm, sizeof(key.comm));
    opens.increment(key);
    return 0;
}
"""

# Load the BPF program
b = BPF(text=bpf_text)
b.attach_tracepoint(tp="syscalls:sys_enter_openat", fn_name="count_opens")

# Run and print results
print("Counting file opens... Press Ctrl+C to stop.")
try:
    time.sleep(9999)
except KeyboardInterrupt:
    pass

print("\n{:<16} {:<10}".format("PROCESS", "OPENS"))
# ## CHANGED: Sort by the .value of the map item
for k, v in sorted(b["opens"].items(), key=lambda item: item[1].value):
    print("{:<16} {:<10}".format(k.comm.decode('utf-8'), v.value))
