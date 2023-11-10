# Assignment_2_CN

### Team Members

- **Karan Bhardwaj** - Roll Number: 20110093

- **Manpreet Singh** - Roll Number: 20110109

## Commands To execute the Q1.py

- Execute the command: **sudo mn -c ; python3 Q1.py**

- sudo mn -c is used to close the topology already in use.

Now, after this command Mininet CLI will open, run the following commands
---
for part a.
---
 mininet> pingall
- To find all host and routers are connected with other properly
---
for part b.
---
 mininet> xterm h1 ra h6
- To open terminal corresponding to h1,h6 host and ra router
- run **wireshark** in ra terminal
- run **pinng 100.103.0.101 -c 3** to send three packets to h6 from h1
- wireshark will capture
---
for part c.
---
mininet> xterm h1 h6 
- To open terminal corresponding to h1 and h6 host. \
Using ping 
- use **ifconfig** in h6 terminal to find the ip of h6
- run **ping 100.103.0.101 -c 3** to find the latency \
Using perf
- use **iperf -s -u -i 1** to start listening on h6
- run **iperf -c 100.103.0.101 -u -b** in h1 terminal to make connection with h6 and send packets
---
for part d
---
Took screenshot after we ran **sudo mn -c ; python3 Q1.py**


