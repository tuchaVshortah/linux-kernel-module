#Keylogger

As you can see it has 2 versions. The first one is ***only capable of capturing key strokes and logging them***,
whereas the second one is ***capable of capturing key strokes and sending them to the userspace*** via a character device.

*Character device allows programs to send characters through them. It works as a pipe that can be connected to another program.
This is needed to allow userspace programs to interact with output of kernel space programs.*

