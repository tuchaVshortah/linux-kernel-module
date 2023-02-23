# linux-kernel-module
OSC final assessment project

The ***build-essential*** package contains tools like ***gcc*** and ***make***, while ***linux-headers-$(uname -r)*** provides the kernel headers for your current kernel version.

Steps to reproduce:
  1. Install the reqiured build essentials on Debian based distributions using this command:
      ***sudo apt-get install build-essential linux-headers-$(uname -r)***
   
      ![image](https://user-images.githubusercontent.com/71591558/220911247-7ea5accb-4b92-447c-a48b-dfa67e8d18c1.png)
  
  2. Build the module with this command:
      ***make -C /lib/modules/$(uname -r)/build M=$PWD modules***
  
      ![image](https://user-images.githubusercontent.com/71591558/220914657-c8fa85ca-8a9c-4fbe-85b7-762fd4a243eb.png)

  3. You can use the insmod or modprobe command to insert the module into your kernel:
  
      ***sudo insmod hello.ko***
