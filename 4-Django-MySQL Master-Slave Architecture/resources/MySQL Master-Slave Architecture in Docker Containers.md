# MySQL Master-Slave Architecture in Docker Containers

[⬅️ Go back to README.md](../README.md)

### Docker Network

Create a docker network for the configuration:

    docker network create replication-net

### Master DB Configuration

1.  Spin up a MySQL container using the following command:

        docker run -d
            --name mysql-master
            --net replication-net
            -e MYSQL_ROOT_PASSWORD=root
            -v "path/of/the/host/machine:/var/lib/mysql"
            -p <host-port>:<container-port>
            mysql:latest
            --server-id=1
            --log-bin=mysql-bin
            --gtid_mode=ON
            --enforce_gtid_consistency=ON

2.  Access into this container to make some further configuration, so that the slave DB can operate replication.

        docker exec -it mysql-master mysql -u root -p

    <small>💡 _Note: Provide the default password ("**root**")_</small>

3.  Create a user record, so that the slave DB can connect with the master DB using this user credentials.

        CREATE USER 'replication_slave'@'%' IDENTIFIED BY 'password';

    3.1# Grant this user with the special replication permission on this DB server.

        GRANT REPLICATION SLAVE ON '*' to 'replication_slave'@'%';

    3.2# Make immediate effect on the `grant` table in the DB.

        FLUSH PRIVILEGES;

4.  View the currently used binary log file & it's position in the memory.

        SHOW BINARY LOG STATUS;

    <small>💡 _Note: Take notes of the bin-log file name (mysql-bin.0000x) & it's position (xyz)_</small>

### Slave DB Configuration

1.  Spin up another MySQL server container using the following command:

        docker run -d
            --name mysql-slave
            --net replication-net
            -e MYSQL_ROOT_PASSWORD=root
            -v "path/of/the/host/machine:/var/lib/mysql"
            -p <host-port>:<container-port>
            mysql:latest
            --server-id=2
            --log-bin=mysql-bin
            --gtid_mode=ON
            --enforce_gtid_consistency=ON

2.  Execute the following config command to assign this DB server for replication from the master DB.

        CHANGE REPLICATION SOURCE TO
            SOURCE_HOST='mysql-master',
            SOURCE_USER='replication_slave',
            SOURCE_PASSWORD='password',
            SOURCE_AUTO_POSITION=1;

    <small>💡 _Note: The `SOURCE_AUTO_POSITION=1` configs the slave DB to automatically read from the bin-log file currently used by master DB._</small>

3.  Start the replications process using the command:

        START REPLICA;

4.  Ensure the slave replication is running properly using the command:

        SHOW REPLICA STATUS\G

    Especially look for the values of two keys (**`Slave_IO_Running`** & **`Slave_SQL_Running`**). If they both have the value "**YES**", it denotes the replication process is successfully running.

![Django + MySQL Primary–Replica Replication Architecture Diagram](./Django%20DB%20Master-Slave%20Architecture.jpg)

<hr>

### <u>APPENDIX</u>

By creating a docker network & assign containers to that network provides the following advantages:

1. A container can invoke another by it's name.

2. Container's by default get IPs dynamically every time it reboots. Docker network solves the issue since the containers can communicate through their container names.

3. Ensure enhanced security & isolation. Containers from outside the network cannot communicate with those DBs other than the app-server containers in the same network.

4. _Optional in this context, since the slave's container port is published to the host port in order to let the Django app to read from the slave DB as the app server is not containerized._

   Inside the custom network, containers can share data using the same port. It avoids conflict with the host machine. i.e. When master & slave DBs exist inside a docker network, they can communicate with each other by sitting in their own private islands (containers), both running internally in port `3306`. Docker network creates a private communication bridge for the containers.
