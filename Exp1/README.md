
# Exp.1 Downloading and installing Hadoop, Understanding different Hadoop modes,


## Aim

To download and install Hadoop, Understanding different Hadoop modes, Startup
scripts, Configuration files.

## Procedure

#### Step 1 : Install Java Development Kit

The default Ubuntu repositories contain Java 8 and Java 11 both. But, Install Java 8 because
hive only works on this version. Use the following command to install it. 

```shell
sudo dnf update && sudo dnf install java-1.8-openjdk 
```

#### Step 2 : Verify the Java version
Once installed, verify the installed version of Java with the following command:

```shell 
javac -version
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-32-20.png)

#### Step 3: Install SSH 

SSH (Secure Shell) installation is vital for Hadoop as it enables secure communication between
nodes in the Hadoop cluster. This ensures data integrity, confidentiality, and allows for efficient
distributed processing of data across the cluster

```shell 
systemctl enable sshd && systemctl start sshd

```
#### Step 4 : Create the hadoop user :

All the Hadoop components will run as the user that you create for Apache Hadoop, and the
user will also be used for logging in to Hadoop’s web interface.
Run the command to create user and set password:

```shell
sudo useradd hadoop
```
```shell
passwd hadoop
```
#### Step 5 : Switch user
Switch to the newly created hadoop user:

```shell
su hadoop
```
#### Step 6 : Configure SSH
Now configure password-less SSH access for the newly created hadoop user, so didn’t enter the
key to save file and passphrase. Generate an SSH keypair (generate Public and Private Key
Pairs)first

```shell
ssh-keygen -t rsa
```

#### Step 7 : Set permissions :
Next, append the generated public keys from id_rsa.pub to authorized_keys and set proper
permission:

```shell
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
```shell
chmod 640 ~/.ssh/authorized_keys
```

#### Step 8 : SSH to the localhost

Next, verify the password less SSH authentication with the following command:

```shell
 ssh localhost
```
#### Step 9 : Switch user

Again switch to hadoop. So, First, change the user to hadoop with the following command:

```shell
su hadoop
```
#### Step 10 : Install hadoop
Next, download the latest version of Hadoop using the wget command:

```shell
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

```

Once downloaded, extract the downloaded file:

```shell
tar -xvzf hadoop-3.3.6.tar.gz 
```
Next, rename the extracted directory to hadoop:

```shell
mv hadoop-3.3.6 hadoop
```
Next, you will need to configure Hadoop and Java Environment Variables on your system. Open
the ~/.bashrc file in your favorite text editor. Use nano editior , to pasting the code we use
ctrl+shift+v for saving the file ctrl+x and ctrl+y ,then hit enter:

Next, you will need to configure Hadoop and Java Environment Variables on your system.

Open the ~/.bashrc file in your favorite text editor:

```shell
nano ~/.bashrc
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-33-07.png)

Save and close the file. Then, activate the environment variables with the following
command:

```shell
source ~/.bashrc
```
Next, open the Hadoop environment variable file:

Search for the *export JAVA_HOME* and configure it.

```shell
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-33-31.png)

Save and close the file when you are finished.

#### Step 11 : Configuring Hadoop :
First, you will need to create the namenode and datanode directories inside the Hadoop user
home directory. Run the following command to create both directories:

```shell
cd hadoop/ && mkdir -p ~/hadoopdata/hdfs/{namenode,datanode}
```

* Next, edit the core-site.xml file and update with your system hostname:

```shell
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-33-46.png)

Change the following name as per your system hostname:
Save and close the file.

Then, edit the hdfs-site.xml file:

```shell
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

* Change the NameNode and DataNode directory paths:

* Then, edit the mapred-site.xml file:

```shell
nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```
Make the following changes
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-34-20.png)


* Then, edit the yarn-site.xml file:
```shell
nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```
Make the following changes
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-34-08.png)
Save the file and close it.

#### Step 12 – Start Hadoop Cluster

Before starting the Hadoop cluster. You will need to format the Namenode as a hadoop user.
Run the following command to format the Hadoop Namenode:

```shell
hdfs namenode –format
```
Once the namenode directory is successfully formatted with hdfs file system, you will see the
message *Storage directory /home/hadoop/hadoopdata/hdfs/namenode has been successfully
formatted.*

Then start the Hadoop cluster with the following command
```shell
start-all.sh
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-35-19.png)

You can now check the status of all Hadoop services using the jps command:

```shell
jps
```
#### Step 13 – Access Hadoop Namenode and Resource Manager

Here my ip address is 192.168.1.6.
* To access the Namenode, open your web browser and visit the URL http://your-serverip:9870.
* You should see the following screen: http://192.168.1.6:9870

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-36-27.png)

To access Resource Manage, open your web browser and visit the URL http://your-serverip:8088. You should see the following screen:

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp1/Images/Screenshot%20from%202024-09-16%2016-36-40.png)

#### Step 14 – Verify the Hadoop Cluster

At this point, the Hadoop cluster is installed and configured. Next, we will create some
directories in the HDFS filesystem to test the Hadoop.

Let’s create some directories in the HDFS filesystem using the following command:

```shell 
hdfs dfs -mkdir /test1 && hdfs dfs -mkdir /logs 
```
Next, run the following command to list the above directory:

```shell
hdfs dfs -ls /
```
Also, put some files to hadoop file system. For the example, putting log files from host
machine to hadoop file system.

```shell
hdfs dfs -put /var/log/* /logs/
```

You can also verify the above files and directory in the Hadoop Namenode web interface.
Go to the web interface, click on the Utilities => Browse the file system. You should see your
directories which you have created earlier.

#### Step 15 – Stop Hadoop Cluster

To stop the Hadoop all services, run the following command:

```shell
stop-all.sh 
```

## Result

The step-by-step installation and configuration of Hadoop on Ubutu linux system have been
successfully completed.