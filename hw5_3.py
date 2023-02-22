def sanitize_phone_number(phone=str):
    return str(phone).replace(" ", "").replace("+", "").replace("(", "").replace(")", "").replace("-", "")


if __name__ == "__main__":
    sanitize_phone_number("    +38(050)123-32-34")