
# Exp.1 Downloading and installing Hadoop, Understanding different Hadoop modes,


## AIM

To Download and install Hadoop, Understanding different Hadoop modes, Startup
scripts, Configuration files.

## PROCEDURE

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

