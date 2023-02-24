# linux-kernel-module
OSC final assessment project

### |===> ***Refer to manual if you want to know how to build modules for the Linux kernel.*** <===|

### |===> ***The keylogger directory contains a module that captures key strokes*** <===|

The ***build-essential*** package contains tools like ***gcc*** and ***make***, while ***linux-headers-$(uname -r)*** provides the kernel headers for your current kernel version.

Steps to reproduce:
  1. Install the reqiured build essentials on Debian based distributions using this command:
      ***sudo apt-get install build-essential linux-headers-$(uname -r)***
   
      ![image](https://user-images.githubusercontent.com/71591558/220911247-7ea5accb-4b92-447c-a48b-dfa67e8d18c1.png)
  
  2. Build the module with this command (or just run *make*):
      ***make -C /lib/modules/$(uname -r)/build M=$PWD modules***
  
      ![image](https://user-images.githubusercontent.com/71591558/220914657-c8fa85ca-8a9c-4fbe-85b7-762fd4a243eb.png)

  3. You can use the insmod or modprobe command to insert the module into your kernel:
  
      ***sudo insmod hello.ko***
  
  4. Run this command to make sure the module has been loaded by the kernel: 
  
      ***sudo dmesg***
      
      ![image](https://user-images.githubusercontent.com/71591558/220915557-5e165f3c-fc0b-448a-9de3-7f6e5e3dee82.png)

  5. To remove the module from your kernel use this command: 

      ***sudo rmmod hello***
      
  6. Verify if it has been removed using the dmesg command. The module should send a ***goodbye*** log message:

      ![image](https://user-images.githubusercontent.com/71591558/220928985-b97cce21-6939-4aff-8a35-730186aa69b9.png)
      
      ![image](https://user-images.githubusercontent.com/71591558/220929142-dad90dcc-bec6-4463-9199-882336f805fa.png)

