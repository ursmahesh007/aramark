from sshtunnel import SSHTunnelForwarder
tunnel = SSHTunnelForwarder(
    '40.121.95.225',
    ssh_username="testuser",
    ssh_password="Windows@1234",
    remote_bind_address=('127.0.0.1', 27017)
)

tunnel.start()
localPort = tunnel.local_bind_port