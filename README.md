# Assignment_2_CN

### Team Members

- **Karan Bhardwaj** - Roll Number: 20110093

- **Manpreet Singh** - Roll Number: 20110109

---
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

Now, make change in the topology and again execute the above commands

---
for part d
---
Took screenshot of routing table for all routers for both case after we ran **sudo mn -c ; python3 Q1.py** separately after making changes in the topology.


---
## Commands To execute the Q2.py

---
for part a.
---

- Execute the command: **sudo mn -c ; python3 Q2.py**
- The messages sent from h1, h2, h3 clients and the acknowledge message from server gets saved in a text file.

---
for part b.
---

- Execute the command: **sudo mn -c; python3 Q2.py --config=b --congestion={congestion_mechanism}**
- congestion_mechanism avaiable [reno, bbr, vegas, cubic]
- output will be a text file containing all throughput information along with bandwidth
- 4 files will be generated in response to 4 congestion_mechanism

---
for part c.
---

- Execute the command: **sudo mn -c; python3 Q2.py --config=c --congestion={congestion_mechanism}**
- congestion_mechanism avaiable [reno, bbr, vegas, cubic]
- output will be a text file containing all throughput information along with bandwidth
- 4 files will be generated in response to 4 congestion_mechanism

---
for part d.
---

- Execute the command: **sudo mn -c; python3 Q2.py --config=d --congestion={congestion_mechanism} --loss={loss %}**
- congestion_mechanism avaiable [reno, bbr, vegas, cubic]
- loss % [1,3]
- output will be a text file containing all throughput information along with bandwidth
- 8 files will be generated in response to 4 congestion_mechanism and 2 loss %




