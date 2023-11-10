# Q2.py

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCIntf
import argparse

class Mytopo(Topo):
    def build(self, **_opts):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3') 
        h4 = self.addHost('h4') 
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s1, s2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mininet script with congestion control')
    parser.add_argument('--config', default='a', choices=['a', 'b', 'c', 'd'], help='Configuration (a, b, c, or d)')
    parser.add_argument('--congestion', default=None, help='Congestion control algorithm (e.g., cubic, vegas, reno, bbr)')
    parser.add_argument('--loss', type=float, default=0, help='Loss percentage for the s1-s2 link')
    args = parser.parse_args()

    setLogLevel('info')
    mytopo = Mytopo()
    net = Mininet(topo=mytopo, intf=TCIntf, waitConnected=True)
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')


    if args.config == 'b':
        # Set congestion control algorithm on h4
        h4.cmd(f'sysctl -w net.ipv4.tcp_congestion_control={args.congestion}')

        # Set congestion control algorithm on h1
        h1.cmd(f'sysctl -w net.ipv4.tcp_congestion_control={args.congestion}')

        h4.cmd(f'iperf -s -i 1 > p2-{args.congestion}.txt &')
        h1.cmd(f'iperf -c 10.0.0.4 -t 30')
            
    elif args.config == 'c':
        # Set congestion control algorithm on h4
        h4.cmd(f'sysctl -w net.ipv4.tcp_congestion_control={args.congestion}')

        # Set congestion control algorithm on h1, h2, and h3
        for client in [ h1, h2, h3]:
            client.cmd(f'sysctl -w net.ipv4.tcp_congestion_control={args.congestion}')

        h4.cmd(f'iperf -s -i 1 > p3-{args.congestion}.txt &')        
        for client in [ h1, h2]:
            client.cmd(f'iperf -c 10.0.0.4 -t 30 &')
        
        h3.cmd(f'iperf -c 10.0.0.4 -t 30')

    elif args.config == 'd':
        # Set loss parameter for Part D on s1-s2 link
        link_s1_s2 = net.linksBetween(net.getNodeByName('s1'), net.getNodeByName('s2'))[0]
        link_s1_s2.intf1.config(loss=args.loss)

        # Set congestion control algorithm on h4
        h4.cmd(f'sysctl -w net.ipv4.tcp_congestion_control={args.congestion}')

        # Set congestion control algorithm on h1
        h1.cmd(f'sysctl -w net.ipv4.tcp_congestion_control={args.congestion}')

        h4.cmd(f'iperf -s -i 1 > p4-{args.congestion}_l{args.loss}.txt &')
        h1.cmd(f'iperf -c 10.0.0.4 -t 30')
    else:
        # Part a
        h4.cmd(f'python3 server.py &')

        for client in ['h1', 'h2', 'h3']:
            net.get(client).cmd('python3 client.py')

    CLI(net)
    net.stop()
