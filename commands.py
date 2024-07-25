import random

commands = {
    "ssh": "Securely connect to a remote server using the SSH protocol.",
    "ls": "List files and directories in the current directory.",
    "pwd": "Print the current working directory path.",
    "cd": "Change the current working directory.",
    "touch": "Create an empty file or update the timestamp of an existing file.",
    "echo": "Output text to the terminal or a file.",
    "nano": "Open and edit files in the nano text editor.",
    "vim": "Open and edit files in the vim text editor.",
    "cat": "Concatenate and display the contents of a file.",
    "shred": "Overwrite a file to securely delete it.",
    "mkdir": "Create a new directory.",
    "cp": "Copy files or directories.",
    "mv": "Move or rename files or directories.",
    "rm": "Remove files or directories.",
    "rmdir": "Remove an empty directory.",
    "ln": "Create a hard or symbolic link to a file.",
    "clear": "Clear the terminal display.",
    "useradd": "Create a new user account.",
    "sudo": "Execute a command as the superuser or another user.",
    "adduser": "Add a new user account (user-friendly).",
    "su": "Switch to another user account.",
    "exit": "Exit the current terminal session.",
    "sudo passwd": "Change the superuser (root) password.",
    "sudo passwd [username]": "Change the password of a specified user.",
    "sudo apt": "Manage packages on Debian-based systems.",
    "sudo apt update & install": "Update package lists and install new packages.",
    "finger": "Display information about system users.",
    "man": "Display the manual page for a command.",
    "whatis": "Display a brief description of a command.",
    "which": "Show the full path of a command.",
    "whereis": "Locate the binary, source, and manual page files for a command.",
    "wget": "Download files from the web via HTTP, HTTPS, and FTP.",
    "curl": "Transfer data from or to a server using various protocols.",
    "zip": "Compress files into a ZIP archive.",
    "unzip": "Extract files from a ZIP archive.",
    "less": "View the contents of a file one page at a time.",
    "head": "Display the first part of a file.",
    "tail": "Display the last part of a file.",
    "cmp": "Compare two files byte by byte.",
    "diff": "Compare files line by line and show differences.",
    "sort": "Sort lines of text files.",
    "find": "Search for files in a directory hierarchy.",
    "chmod": "Change the file mode (permissions).",
    "chown": "Change file owner and group.",
    "ifconfig": "Configure or display network interface parameters.",
    "ip address": "Display or manage IP addresses and routing.",
    "ping": "Send ICMP echo requests to network hosts.",
    "netstat": "Display network connections, routing tables, and interface statistics.",
    "ss": "Display socket statistics.",
    "iptables": "Set up, maintain, and inspect the IP packet filter rules.",
    "ufw": "Manage firewall rules with Uncomplicated Firewall.",
    "uname": "Print system information.",
    "neofetch": "Display system information with an ASCII logo.",
    "cal": "Display a calendar.",
    "free": "Show the amount of free and used memory in the system.",
    "df and df -h": "Report file system disk space usage.",
    "ps": "Report a snapshot of current processes.",
    "top": "Display tasks and system resource usage in real-time.",
    "kill": "Send a signal to terminate a process.",
    "systemctl": "Control the systemd system and service manager.",
    "history": "Show the command history list.",
    "sudo reboot": "Reboot the system.",
    "shutdown": "Power off or reboot the system."
}

while True:
    command, definition = random.choice(list(commands.items()))
    print(f"Definition: {definition}")
    user_input = input("Enter the command: ").strip()

    if user_input == command:
        print("Correct! Moving to the next definition.\n")
    else:
        print(f"Incorrect. The correct command was: {command}. Exiting the script.")
        break
