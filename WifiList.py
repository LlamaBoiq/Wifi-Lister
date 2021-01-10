import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]
running = True
def void():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while running == True:
    for wifi in wifis:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1]
        for line in results if 'Key Content' in line]
        try:
            print(f"Name: {wifi} \n Password: {results[0]} \n")
        except IndexError:
            print(f'Name: {wifi} \n Password: Couldnt fetch password')
        except KeyboardInterrupt:
            break

    input()
    void()