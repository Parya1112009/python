import paramiko
import pdb;
router_ip = "172.16.1.100"
router_username = "admin"
router_password = "admin1"
ssh = paramiko.SSHClient()
pdb.set_trace()
def run_command_on_device(ip_address, username, password, command):
    """ Connect to a device, run a command, and return the output."""
    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    total_attempts = 3
    for attempt in range(total_attempts):
        try:
            print("Attempt to connect: %s" % attempt)
            # Connect to router using username/password authentication.
            ssh.connect(router_ip, 
                        username=router_username, 
                        password=router_password,
                        look_for_keys=False )
            # Run command.
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            # Read output from command.
            output = ssh_stdout.readlines()
            # Close connection.
            ssh.close()
            return output
        except Exception as error_message:
            print("Unable to connect")
            print(error_message)