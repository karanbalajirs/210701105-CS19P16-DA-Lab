# Exp5: Installation of Hive on Ubuntu

## Aim
To Download and install Hive, Understanding Startup scripts, Configuration files.
## Procedure

#### Step 1: Download and extract it

Download the Apache hive and extract it use tar, the commands given below:

```shell
wget https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz

tar –xvf apache-hive-3.1.2-bin.tar.gz
```

#### Step 2: Place different configuration properties in Apache Hive
In this step, we are going to do two things
* Placing Hive Home path in bashrc file
```shell
nano .bashrc
```
And append the below lines in it.

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp5/5-Images/Screenshot%20from%202024-09-16%2016-44-35.png)

* Exporting Hadoop path in Hive-config.sh (To communicate with the Hadoop ecosystem we are defining Hadoop Home path in hive config field) Open the hiveconfig.sh as shown in below.
```shell
cd apache-hive-3.1.2-bin/bin
```
```shell
cp hive-env.sh.template hive-env.sh
```
```shell
nano hive-env.sh
```
*Append the below commands on it*

```shell
export HADOOP_HOME=/home/Hadoop/Hadoop
export HIVE_CONF_DIR=/home/Hadoop/apache-hive-3.1.2/conf
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp5/5-Images/Screenshot%20from%202024-09-16%2016-45-07.png)

#### Step 3: Install mysql

1.Install mysql in Fedora by running this command: 

```shell
sudo dnf update
sudo dnf install mysql-server
systemctl enable mysqld
systemctl start mysqld
```

2.Alter username and password for MySQLby running below commands:

```shell
sudo mysql
```

Pops command line interface for MySQLand run the below SQL queries to change username and set password.

```mysql
SELECT user, host, plugin FROM mysql.user WHERE user = 'root';
```

```mysql
> ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY
'your_new_password';
```

```mysql
FLUSH PRIVILEGES;
```

#### Step 4:Config hive-site.xml

Config the hive-site.xml by appending this xml code and change the username and password according to your MySQL.

```shell
cd apache-hive-3.1.2-bin/bin
cp hive-default.xml.template hive-site.xml
nano hive-site.xml
```

*Append these lines into it*

*Replace root as your username of MySQL*

*Replaceyour_new_password as with your password of MySQL*

```xml

<configuration>
        <property>
            <name>javax.jdo.option.ConnectionURL</name>
            <value>jdbc:mysql://localhost/metastore?createDatabaseIfNotExist=true</value>
        </property>
        <property>
            <name>javax.jdo.option.ConnectionDriverName</name>
            <value>com.mysql.cj.jdbc.Driver</value>
        </property>
        <property>
            <name>javax.jdo.option.ConnectionUserName</name>
            <value>root</value>
        </property>
        <property>
            <name>javax.jdo.option.ConnectionPassword</name>
            <value>your_new_password</value>
        </property>
        <property>
            <name>datanucleus.autoCreateSchema</name>
            <value>true</value>
        </property>
        <property>
            <name>datanucleus.fixedDatastore</name>
            <value>true</value>
        </property>
        <property>
            <name>datanucleus.autoCreateTables</name>
            <value>True</value>
        </property>
</configuration>

```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp5/5-Images/Screenshot%20from%202024-09-16%2016-46-01.png)

#### Step 5: Setup MySQL java connector:
*First, you'll need to download the MySQL Connector/J, which is the JDBC driver for
MySQL. You can download it from the below link*

[MySql JDBC Connector](https://drive.google.com/file/d/1QFhB7Kvcat7a4LzDRe6GcmZva1yAxKz-/view?usp=drive_link)

*Copy the downloaded MySQL Connector/J JAR file to the Hive library directory. By default,
the Hive library directory is usually located at/path/to/apache-hive-3.1.2/lib/on Ubuntu. Use
the following command to copy the JAR file:*

```shell
sudo cp /path/to/mysql-connector-java-8.0.15.jar /path/to/apache-hive-3.1.2/lib/
```
*Replace /path/to/ with the actual path to the JAR file.*

#### Step 6:Initialize the Hive Metastore Schema:
*Run the following command to initialize the Hive metastore schema:*
```shell
schematool -initSchema -dbTypemysql
```

#### Step 7: Start hive:
You can test Hive by running the Hive shell: Copy code hive You should be able to run Hive queries, and metadata will be stored in your MySQL database.

```shell
hive
```

## Result
Thus, the Apache Hive installation is completed successfully on Fedora.