from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter(Node):

    "A Node with IP forwarding enabled."

    def config(self, **params):

        super(LinuxRouter, self).config(**params)

        # Enable forwarding on the router

        self.cmd('sysctl net.ipv4.ip_forward=1')


    def terminate(self):

        self.cmd('sysctl net.ipv4.ip_forward=0')

        super(LinuxRouter, self).terminate()


class NetworkTopo(Topo):

    # Creating the custom topology

    def build(self, **_opts):

        # subnet1 = '100.101.1.0/24'
        # subnet2 = '100.102.0.0/24'
        # subnet3 = '100.103.0.0/24'

        s1, s2, s3 = [ self.addSwitch( s ) for s in ( 's1', 's2', 's3' ) ]

        ra,rb,rc=[self.addNode(s,cls=LinuxRouter,ip=a) for s,a in[('ra','100.101.1.1/24'),('rb','100.102.0.1/24'),('rc','100.103.0.1/24')]]
        
        h1,h2=[self.addHost(h,ip=a,defaultRoute='via 100.101.1.1')for h,a in [('h1','100.101.1.100/24'),('h2','100.101.1.101/24')]]
        h3,h4=[self.addHost(h,ip=a,defaultRoute='via 100.102.0.1')for h,a in [('h3','100.102.0.100/24'),('h4','100.102.0.101/24')]]
        h5,h6=[self.addHost(h,ip=a,defaultRoute='via 100.103.0.1')for h,a in [('h5','100.103.0.100/24'),('h6','100.103.0.101/24')]]

        # Connect subnets to routers
        for s,r,b,c in[(s1,ra,'ra-eth1','100.101.1.1/24'),(s2,rb,'rb-eth1','100.102.0.1/24'),(s3,rc,'rc-eth1','100.103.0.1/24')]:
            self.addLink(s,r,intfName2=b,params2={'ip':c} )

        
        for h,s in [(h1,s1),(h2,s1),(h3,s2),(h4,s2),(h5,s3),(h6,s3)]:
            self.addLink(h,s)

        for r1,r2,a,b,c,d in[(ra,rb,'l','m','200.100.1.1/24','200.100.1.2/24'),(rb,rc,'n','o','200.100.2.1/24','200.100.2.2/24'),(ra,rc,'p','q','200.100.3.1/24','200.100.3.2/24')]:
            self.addLink(r1,r2,intfName1=a,intfName2=b,params1={'ip':c},params2={'ip':d})



if __name__ == '__main__':

    setLogLevel('info')

    topo = NetworkTopo()

    net = Mininet(topo=topo, waitConnected=True)

    # Add static routes on ra

    net['ra'].cmd('ip route add 100.102.0.0/24 via 200.100.1.2')

    net['ra'].cmd('ip route add 100.103.0.0/24 via 200.100.1.2')

    # Add static routes on rb

    net['rb'].cmd('ip route add 100.101.1.0/24 via 200.100.1.1')

    net['rb'].cmd('ip route add 100.103.0.0/24 via 200.100.2.2')

    # Add static routes on rc

    net['rc'].cmd('ip route add 100.101.1.0/24 via 200.100.3.1')

    net['rc'].cmd('ip route add 100.102.0.0/24 via 200.100.2.1')



    net.start()

    info('*** Adding static routes on routers:\n')


    info('*** Routing Tables on Routers:\n')

    for router in ['ra', 'rb', 'rc']:

        info(net[router].cmd('route'))

    CLI(net)

    net.stop()