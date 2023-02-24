# Compilation and usage


Steps to reproduce:
  1. Install *(skip if installed)* the reqiured build essentials on Debian based distributions using this command:
      ***sudo apt-get install build-essential linux-headers-$(uname -r)***
   
      ![image](https://user-images.githubusercontent.com/71591558/220911247-7ea5accb-4b92-447c-a48b-dfa67e8d18c1.png)
  
  2. Build the module with this command:
      ***make -C /lib/modules/$(uname -r)/build M=$PWD modules***
  
      ![image](https://user-images.githubusercontent.com/71591558/221275415-7c166a51-c3c6-4617-839f-614218e53c81.png)

  3. You can use the insmod or modprobe command to insert the module into your kernel:
  
      ***sudo insmod keylogger.ko***
  
  4. Run this command to make sure the module has been loaded by the kernel: 
  
      ***dmesg***
      
      ![image](https://user-images.githubusercontent.com/71591558/221278584-4bc14e3e-441d-41df-8ac7-6caa7b2491ab.png)

  5. To remove the module from your kernel use this command: 

      ***sudo rmmod keylogger***
      
  6. Verify if it has been removed using the dmesg command. The module should send a ***goodbye*** log message:

      ![image](https://user-images.githubusercontent.com/71591558/221278843-ea4c0d86-469a-48ec-8309-199eaeece5d2.png)
