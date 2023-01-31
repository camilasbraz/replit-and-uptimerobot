from schedule import *

schedule()

# Update every 24 hours
time_to_wait = 24


def loop():
    while True:
        try:
            playlistGen()
            print(f'\nNice!!!!\n')
            time.sleep(time_to_wait * 3600)
        except Exception as e:
            print(f'\Exception:\n{e}\n\n{traceback.format_exc()}\n\n')
            time.sleep(600)
            continue

if __name__ == '__main__':
    loop()
