def get_todo():
    with open(r"E:\TKH Git\Innovation Fellowship 2023\tkh_if_dsc_23_student\1.04\10_24\code_along\data\todo.txt") as f:
        lines = f.readlines()

        for row in lines:
            print(row)

if __name__ == "__main__": #is the main
    print("youve ran todo.py")
