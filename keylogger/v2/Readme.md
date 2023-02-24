# Compilation and usage

Steps to reproduce:
  1. Install *(skip if installed)* the reqiured build essentials on Debian based distributions using this command:
      ***sudo apt-get install build-essential linux-headers-$(uname -r)***
   
      ![image](https://user-images.githubusercontent.com/71591558/220911247-7ea5accb-4b92-447c-a48b-dfa67e8d18c1.png)
  
  2. Build the module with this command:
      ***make -C /lib/modules/$(uname -r)/build M=$PWD modules***
  
      ![image](https://user-images.githubusercontent.com/71591558/221279377-a54f7f5e-50b1-4971-8301-a5c59bc7e818.png)
      
  3. You can use the insmod or modprobe command to insert the module into your kernel:
  
      ***sudo insmod keylogger2.ko***
  
  4. Run this command to make sure the module has been loaded by the kernel: 
  
      ***dmesg***
      
      ![image](https://user-images.githubusercontent.com/71591558/221279731-abaae9f5-d2d3-47c0-8d38-68a795fec7a5.png)

  5. To remove the module from your kernel use this command: 

      ***sudo rmmod hello***
      
  6. Verify if it has been removed using the dmesg command. The module should send a ***goodbye*** log message:

      ![image](https://user-images.githubusercontent.com/71591558/221279825-d7b8522f-911f-4ac5-88b7-1dd8b4e5eea6.png)
      
  7. Get the major number from the forth step and run this command:

      ***mknod keylog0 c <your_major_number_here> 0***
  
  8. Then go to the GUI folder and start it.
