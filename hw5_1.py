def real_len(text=str):

    map = {ord('\n'): '', ord('\f'): '', ord('\r')
               : '', ord('\t'): '', ord('\v'): ''}
    real_str = text.translate(map)
    return len(real_str)


if __name__ == "__main__":
    real_len('Alex\nKdfe23\t\f\v.\r')


# +
