def capture_username():
    return input("What's your name? ")


def greeting(username):
    print("Hello,", username)


if __name__ == "__main__":
    username = capture_username()
    greeting(username)
