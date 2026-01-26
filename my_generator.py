def genertor(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield print(line.rstrip())


def generator_start(file_name):
    gen = genertor(file_name)
    while True:
        comand = input("введите next чтобы продолжить или stop чтобы остановить программу\n")
        if comand == "stop":
            break
        else:
            try:
                next(gen)
            except StopIteration:
                print("Файл закончился")
                break


generator_start("log.log")
