# File-Sight: A Real-Time Linux File Open Profiler using eBPF



## 🚀 What is File-Sight?

File-Sight is a simple yet powerful command-line tool for Linux that provides a real-time view of the most frequently opened files on your system. It uses eBPF technology to safely and efficiently trace file open events directly from the kernel, offering deep insights into system behavior.

This project was built as a personal learning exercise to understand the fundamentals of eBPF, BCC, and systems programming.

---

## ✨ Features

- **Real-Time Monitoring:** See which files are being accessed across your entire system, live.
- **Top 10 View:** Automatically aggregates and displays the top 10 most active files.
- **Low Overhead:** Built with eBPF to be highly efficient and safe to run on live systems.

---

## 🔧 How it Works

The tool is a Python script that leverages the BCC framework.
1.  An eBPF program written in C is loaded into the kernel.
2.  This program is attached to the `do_sys_openat2` kernel function, which is a key function for handling file opens.
3.  Every time a file is opened, the eBPF program stores the filename in an eBPF map and increments its count.
4.  The Python script reads this map and displays the top 10 results in a clean, formatted table.

---

## 🛠️ How to Use

### Prerequisites
- Linux system with kernel headers installed
- `bpfcc-tools` and `python3-bpfcc`

```bash
# Install dependencies (Debian/Ubuntu)
sudo apt update
sudo apt install bpfcc-tools python3-bpfcc

# Clone the repository
git clone [https://github.com/your-username/ebpf-file-profiler.git](https://github.com/your-username/ebpf-file-profiler.git)
cd ebpf-file-profiler

# Run the tool
sudo ./file_profiler.py
