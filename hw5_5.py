def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    codes = {
        "UA" : [],
        "JP" : [],
        "TW" : [],
        "SG" : []
    }
    for numb in list_phones:
        n_ph = sanitize_phone_number(numb)
        if str(n_ph).startswith("81"):
            codes["JP"].append(n_ph)

        elif str(n_ph).startswith("65"):
            codes["SG"].append(n_ph)

        elif str(n_ph).startswith("886"):
            codes["TW"].append(n_ph)

        elif str(n_ph).startswith("380"):
            codes["UA"].append(n_ph)
        else:
            codes["UA"].append(n_ph)
    return codes



if __name__ == "__main__":
    get_phone_numbers_for_countries(["    +38(050)123-32-34", " +813548657 8"] )