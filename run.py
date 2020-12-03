from instadm import InstaDM
import configparser
from os import chdir
from os.path import exists, dirname, abspath

_author = "Kowshika @ https://kowshika-n.github.io/"
_version = 0.1

current_dir = dirname(abspath(__file__))
chdir(current_dir)
ConfigFilePath = "Config.txt"


def getDataFromConfig(Key):
    """Read Data from Config,ini file and return based on Section and Key"""
    config = configparser.ConfigParser()
    if not exists(ConfigFilePath):
        print(f"Error: Config.txt file not found.")
    else:
        try:
            config.read(ConfigFilePath)
            if not config.has_option("Config", Key):
                print(
                    f"Error: Section 'Config' and Key {Key} not found in Config file."
                )
            else:
                return config["Config"][Key]
        except:
            pass
    return ""


def main():
    """Login to Insta and send message"""
    insta_login_username = getDataFromConfig("InstaLoginUsername")
    insta_login_password = getDataFromConfig("InstaLoginPassword")
    insta_handles_list = getDataFromConfig("InstaHandles").split(",")
    insta_handles = [x.strip() for x in insta_handles_list if x.strip()]
    print(f"Found {len(insta_handles)} instagram users to message")
    insta_message = getDataFromConfig("Message")
    print(f"Message = {insta_message}")
    insta = None

    try:
        # login to insta
        insta = InstaDM(insta_login_username, insta_login_password, False, None)
        # Send message
        for insta_user in insta_handles:
            insta.sendMessage(user=insta_user, message=insta_message)
            insta.__random_sleep__(50, 60)

    except Exception as e:
        print(str(e))
    finally:
        if insta:
            insta.teardown()


if __name__ == "__main__":
    main()
