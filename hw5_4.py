def is_check_name(fullname = str, first_name = str):
    return fullname.startswith(first_name)




if __name__ == "__main__":
    is_check_name("TestHook", "Test")