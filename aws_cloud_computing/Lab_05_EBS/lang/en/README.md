<header>

<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

</header>

<!--include:Logo-->

<style type="text/css">
  body {
      font-family:  "Roboto", "Helvetica", sans-serif;
      font-size: 12pt;
      font-color: Gray;
      line-height: 1.6;
      margin: 50px;
  }
  p {
      list-style-position: inside;
  }
  #ssb_blue {
    background-color: #257ACF;
    font-weight: bold;
    font-size: 90%;
    color: white;
    border-radius: 5px;
    padding-top: 3px;
    padding-bottom: 3px;
    padding-left: 10px;
    padding-right: 10px;
    white-space: nowrap;
  }
  #ssb_voc_grey {
    background-color: #F2F3F4;
    font-weight: normal;
    font-size: 90%;
    color: black;
    border-radius: 3px;
    border: 1px solid gray;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 6px;
    padding-right: 6px;
    white-space: nowrap;
  }
  #ssb_grey {
    background-color: #DEDEDE;
    font-weight: bold;
    font-size: 90%;
    color: #444;
    position: relative;
    top:-1px;
    border-radius: 5px;
    border-width: 1px;
    border-style: solid;
    border-color: #444;
    padding-top: 3px;
    padding-bottom: 3px;
    padding-left: 10px;
    padding-right: 10px;
    white-space: nowrap;
  }
  #ssl_alexa_ocean {
    color: #00a0d2;
    font-weight: bold;
  }
</style>

# Lab 4: Working with EBS

<!-- Note to translators: This is based on SPL-02. Copy the translation from there. Do not re-translate the whole document. -->

<!--Copied from Version 5.1.3 (spl2)-->

## Lab Overview

<img src="../../images/lab-scenario.jpeg" alt="architectural diagram" width="400">

This lab focuses on Amazon Elastic Block Store (Amazon EBS), a key underlying storage mechanism for Amazon EC2 instances. In this lab, you will learn how to create an Amazon EBS volume, attach it to an instance, apply a file system to the volume, and then take a snapshot backup.

## Topics covered

By the end of this lab, you will be able to:

- Create an Amazon EBS volume
- Attach and mount your volume to an EC2 instance
- Create a snapshot of your volume
- Create a new volume from your snapshot
- Attach and mount the new volume to your EC2 instance

## Lab Pre-requisites

To successfully complete this lab, you should be familiar with basic Amazon EC2 usage and with basic Linux server administration. You should feel comfortable using the Linux command-line tools.

### Other AWS Services

Other AWS Services than the ones needed for this lab are disabled by IAM policy during your access time in this lab. In addition, the capabilities of the services used in this lab are limited to what's required by the lab and in some cases are even further limited as an intentional aspect of the lab design. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

### What is Amazon Elastic Block Store?

**Amazon Elastic Block Store (Amazon EBS)** offers persistent storage for Amazon EC2 instances. Amazon EBS volumes are network-attached and persist independently from the life of an instance. Amazon EBS volumes are highly available, highly reliable volumes that can be leveraged as an Amazon EC2 instances boot partition or attached to a running Amazon EC2 instance as a standard block device.

When used as a boot partition, Amazon EC2 instances can be stopped and subsequently restarted, enabling you to pay only for the storage resources used while maintaining your instance's state. Amazon EBS volumes offer greatly improved durability over local Amazon EC2 instance stores because Amazon EBS volumes are automatically replicated on the backend (in a single Availability Zone).

For those wanting even more durability, Amazon EBS provides the ability to create point-in-time consistent snapshots of your volumes that are then stored in Amazon Simple Storage Service (Amazon S3) and automatically replicated across multiple Availability Zones. These snapshots can be used as the starting point for new Amazon EBS volumes and can protect your data for long-term durability. You can also easily share these snapshots with co-workers and other AWS developers.

This lab guide explains basic concepts of Amazon EBS in a step-by-step fashion. However, it can only give a brief overview of Amazon EBS concepts. For further information, see the <a href="http://aws.amazon.com/ebs/" target="_blank">Amazon EBS documentation</a>.

### Amazon EBS Volume Features

Amazon EBS volumes deliver the following features:

- **Persistent storage:** Volume lifetime is independent of any particular Amazon EC2 instance.
- **General purpose:** Amazon EBS volumes are raw, unformatted block devices that can be used from any operating system.
- **High performance:** Amazon EBS volumes are equal to or better than local Amazon EC2 drives.
- **High reliability:** Amazon EBS volumes have built-in redundancy within an Availability Zone.
- **Designed for resiliency:** The AFR (Annual Failure Rate) of Amazon EBS is between 0.1% and 1%.
- **Variable size:** Volume sizes range from 1 GB to 16 TB.
- **Easy to use:** Amazon EBS volumes can be easily created, attached, backed up, restored, and deleted.

**Duration**
This lab takes approximately **30 minutes** to complete.

## Accessing the AWS Management Console

1. At the top of these instructions, click <span id="ssb_voc_grey">Start Lab</span> to launch your lab.

    A Start Lab panel opens displaying the lab status.

2. Wait until you see the message "**Lab status: ready**", then click the **X** to close the Start Lab panel.

3. At the top of these instructions, click <span id="ssb_voc_grey">AWS</span>

    This will open the AWS Management Console in a new browser tab. The system will automatically log you in.

    **Tip**: If a new browser tab does not open, there will typically be a banner or icon at the top of your browser indicating that your browser is preventing the site from opening pop-up windows. Click on the banner or icon and choose "Allow pop ups."

4. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you will be able to see both browser tabs at the same time, to make it easier to follow the lab steps.

&nbsp;
&nbsp;
## Task 1: Create a New EBS Volume

In this task, you will create and attach an Amazon EBS volume to a new Amazon EC2 instance.

5. In the **AWS Management Console**, on the **Services** menu, click **EC2**.

6. In the left navigation pane, click **Instances**.

    An Amazon EC2 instance named **Lab** has already been launched for your lab.

7. Note the **Availability Zone** of the instance. It will look similar to *us-west-2a*.

8. In the left navigation pane, click **Volumes**.

    You will see an existing volume that is being used by the Amazon EC2 instance. This volume has a size of 8 GiB, which makes it easy to distinguish from the volume you will create next, which will be 1 GiB in size.

9. Click <span id="ssb_blue">Create Volume</span> then configure:

    * **Volume Type:** *General Purpose SSD (gp2)*
    * **Size (GiB):** `1`. **NOTE**: You may be restricted from creating large volumes.
    * **Availability Zone:** Select the same availability zone as your EC2 instance.
    * Click <span id="ssb_grey">Add Tag</span>
    * In the Tag Editor, enter:
      * **Key:** `Name`
      * **Value:** `My Volume`

10. Click <span id="ssb_blue">Create Volume</span> then click <span id="ssb_blue">Close</span>

    Your new volume will appear in the list, and will move from the *creating* state to the *available* state. You may need to click **refresh** <span class="fas fa-sync"></span> to see your new volume.

&nbsp;
&nbsp;
## Task 2: Attach the Volume to an Instance

You can now attach your new volume to the Amazon EC2 instance.

11. Select <i class="fas fa-square" style="color:blue"></i> **My Volume**.

12. In the **Actions** menu, click **Attach Volume**.

13. Click in the **Instance** field, then select the instance that appears (Lab).

    Note that the **Device** field is set to */dev/sdf*. You will use this device identifier in a later task.

14. Click <span id="ssb_blue">Attach</span>
The volume state is now *in-use*.

&nbsp;
&nbsp;
## Task 3: Connect to Your Amazon EC2 Instance

### <i class="fab fa-windows"></i> Windows Users: Using SSH to Connect

<i class="fas fa-comment"></i> These instructions are for Windows users only.

If you are using macOS or Linux, <a href="#ssh-MACLinux">skip to the next section</a>.

15. Read through the three bullet points in this step before you start to complete the actions, because you will not be able see these instructions when the Details panel is open.

    * Click on the <span id="ssb_voc_grey">Details</span> drop down menu above these instructions you are currently reading, and then click <span id="ssb_voc_grey">Show</span>. A Credentials window will open.

    * Click on the **Download PPK** button and save the **labsuser.ppk** file. Typically your browser will save it to the Downloads directory.

    * Then exit the Details panel by clicking on the **X**.

16. Download needed software.

    * You will use **PuTTY** to SSH to Amazon EC2 instances. If you do not have PuTTY installed on your computer, <a href="https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe">download it here</a>.

17. Open **putty.exe**

18. Configure PuTTY to not timeout:

    * Click **Connection**
    * Set **Seconds between keepalives** to `30`

    This allows you to keep the PuTTY session open for a longer period of time.

19. Configure your PuTTY session:

    * Click **Session**

    * **Host Name (or IP address):** Copy and paste the **IPv4 Public IP address** for the instance. To find it, return to the EC2 Console and click on **Instances**. Check the box next to the instance and in the *Description* tab copy the **IPv4 Public IP** value.

    * Back in PuTTy, in the **Connection** list, expand <i class="far fa-plus-square"></i> **SSH**

    * Click **Auth** (don't expand it)

    * Click **Browse**

    * Browse to and select the labsuser.ppk file that you downloaded

    * Click **Open** to select it

    * Click **Open**

20. Click **Yes**, to trust the host and connect to it.

21. When prompted **login as**, enter: `ec2-user`

    This will connect you to the EC2 instance.

22. <a href="#ssh-after">Windows Users: Click here to skip ahead to the next task.</a>

<a id='ssh-MACLinux'></a>
### macOS <i class="fab fa-apple"></i> and Linux <i class="fab fa-linux"></i> Users

These instructions are for Mac/Linux users only. If you are a Windows user, <a href="#ssh-after">skip ahead to the next task.</a>

23. Read through all the instructions in this one step before you start to complete the actions, because you will not be able see these instructions when the Details panel is open.

    * Click on the <span id="ssb_voc_grey">Details</span> drop down menu above these instructions you are currently reading, and then click <span id="ssb_voc_grey">Show</span>. A Credentials window will open.

    * Click on the **Download** button and save the **labsuser.pem** file.

    * Then exit the Details panel by clicking on the **X**.

24. Open a terminal window, and change directory `cd` to the directory where the labsuser.pem file was downloaded.

    For example, run this command, if it was saved to your Downloads directory:

    ```plain
    cd ~/Downloads
    ```

25. Change the permissions on the key to be read only, by running this command:

    ```plain
    chmod 400 labsuser.pem
    ```

26. Return to the AWS Management Console, and in the EC2 service, click on **Instances**.

    The **Lab** instance should selected.

27. In the *Description* tab, copy the **IPv4 Public IP** value.

28. Return to the terminal window and run this command (replace **<public-ip\>** with the actual public IP address you copied):

    ```plain
    ssh -i labsuser.pem ec2-user@<public-ip>
    ```

29. Type `yes` when prompted to allow a first connection to this remote SSH server.

    Because you are using a key pair for authentication, you will not be prompted for a password.

<a id='ssh-after'></a>


&nbsp;
&nbsp;
## Task 4: Create and Configure Your File System

In this task, you will add the new volume to a Linux instance as an ext3 file system under the /mnt/data-store mount point.

<i class="fas fa-info-circle"></i> If you are using PuTTY, you can paste text by right-clicking in the PuTTY window.

30. View the storage available on your instance:

    ```plain
    df -h
    ```

    You should see output similar to:

    ```plain
    Filesystem      Size  Used Avail Use% Mounted on
    devtmpfs        488M   60K  488M   1% /dev
    tmpfs           497M     0  497M   0% /dev/shm
    /dev/xvda1      7.8G  982M  6.7G  13% /
    ```

    This is showing the original 8GB disk volume. Your new volume is not yet shown.

31. Create an ext3 file system on the new volume:

    ```plain
    sudo mkfs -t ext3 /dev/sdf
    ```

32. Create a directory for mounting the new storage volume:

    ```plain
    sudo mkdir /mnt/data-store
    ```

33. Mount the new volume:

    ```plain
    sudo mount /dev/sdf /mnt/data-store
    ```

    To configure the Linux instance to mount this volume whenever the instance is started, you will need to add a line to */etc/fstab*.

    ```plain
    echo "/dev/sdf   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab
    ```

34. View the configuration file to see the setting on the last line:

    ```plain
    cat /etc/fstab
    ```

35. View the available storage again:

    ```plain
    df -h
    ```

    The output will now contain an additional line - */dev/xvdf*:

    ```plain
    Filesystem      Size  Used Avail Use% Mounted on
    devtmpfs        488M   60K  488M   1% /dev
    tmpfs           497M     0  497M   0% /dev/shm
    /dev/xvda1      7.8G  982M  6.7G  13% /
    /dev/xvdf       976M  1.3M  924M   1% /mnt/data-store
    ```

36. On your mounted volume, create a file and add some text to it.

    ```plain
    sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"
    ```

37. Verify that the text has been written to your volume.

    ```plain
    cat /mnt/data-store/file.txt
    ```

&nbsp;
&nbsp;
## Task 5: Create an Amazon EBS Snapshot

In this task, you will create a snapshot of your EBS volume.

You can create any number of point-in-time, consistent snapshots from Amazon EBS volumes at any time. Amazon EBS snapshots are stored in Amazon S3 with high durability. New Amazon EBS volumes can be created out of snapshots for cloning or restoring backups. Amazon EBS snapshots can also be easily shared among AWS users or copied over AWS regions.

38. In the **AWS Management Console**, click on **Volumes** and select <i class="fas fa-square" style="color:blue"></i> **My Volume**.

39. In the **Actions** menu, click **Create Snapshot**.

40. Click <span id="ssb_grey">Add Tag</span> then configure:

    * **Key:** `Name`
    * **Value:** `My Snapshot`
    * Click <span id="ssb_blue">Create Snapshot</span> then click <span id="ssb_blue">Close</span>

    Your snapshot will be listed in the **Snapshots** console.

41. In the left navigation pane, click **Snapshots**.

    Your snapshot is displayed. It will start with a state of *pending*, which means that the snapshot is being created. It will then change to a state of *completed*. Only used storage blocks are copied to snapshots, so empty blocks do not take any snapshot storage space.

42. In your remote SSH session, delete the file that you created on your volume.

    ```plain
    sudo rm /mnt/data-store/file.txt
    ```

43. Verify that the file has been deleted.

    ```plain
    ls /mnt/data-store/
    ```

    Your file has been deleted.

&nbsp;
&nbsp;
## Task 6: Restore the Amazon EBS Snapshot

If you ever wish to retrieve data stored in a snapshot, you can **Restore** the snapshot to a new EBS volume.

### Create a Volume Using Your Snapshot

44. In the **AWS Management Console**, select <i class="fas fa-square" style="color:blue"></i> **My Snapshot**.

45. In the **Actions** menu, click **Create Volume**.

46. For **Availability Zone** Select the same availability zone that you used earlier.

47. Click <span id="ssb_grey">Add Tag</span> then configure:

    * **Key:** `Name`
    * **Value:** `Restored Volume`
    * Click <span id="ssb_blue">Create Volume</span>
    * Click <span id="ssb_blue">Close</span>

    When restoring a snapshot to a new volume, you can also modify the configuration, such as changing the volume type, size or Availability Zone.

### Attach the Restored Volume to Your EC2 Instance

48. In the left navigation pane, click **Volumes**.

49. Select <i class="fas fa-square" style="color:blue"></i> **Restored Volume**.

50. In the **Actions** menu, click **Attach Volume**.

51. Click in the **Instance** field, then select the instance that appears (Lab).

    Note that the **Device** field is set to */dev/sdg*. You will use this device identifier in a later task.

52. Click <span id="ssb_blue">Attach</span>

    The volume state is now *in-use*.

### Mount the Restored Volume

53. Create a directory for mounting the new storage volume:

    ```plain
    sudo mkdir /mnt/data-store2
    ```

54. Mount the new volume:

    ```plain
    sudo mount /dev/sdg /mnt/data-store2
    ```

55. Verify that volume you mounted has the file that you created earlier.

    ```plain
    ls /mnt/data-store2/
    ```

    You should see file.txt.

&nbsp;
&nbsp;
## Conclusion

<i class="far fa-thumbs-up" style="color:blue"></i> Congratulations! You now have successfully:

- Created an Amazon EBS volume
- Attached the volume to an EC2 instance
- Created a file system on the volume
- Added a file to volume
- Created a snapshot of your volume
- Created a new volume from the snapshot
- Attached and mounted the new volume to your EC2 instance
- Verified that the file you created earlier was on the newly created volume

## Lab Complete

<i class="icon-flag-checkered"></i> Congratulations! You have completed the lab.

56. Click <span id="ssb_voc_grey">End Lab</span> at the top of this page and then click <span id="ssb_blue">Yes</span> to confirm that you want to end the lab.  

    A panel will appear, indicating that "DELETE has been initiated... You may close this message box now."

57. Click the **X** in the top right corner to close the panel.

## Additional Resources

<a href="http://aws.amazon.com/ebs/" target="_blank">Amazon Elastic Block Store features, functions, and pricing</a>

<a href="http://aws.amazon.com/training/" target="_blank">AWS Training and Certification</a>

For feedback, suggestions, or corrections, please email us at: <aws-course-feedback@amazon.com>
