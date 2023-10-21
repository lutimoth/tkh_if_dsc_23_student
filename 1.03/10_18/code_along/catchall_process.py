import time

data = [130, 500, 1000, "404", 530, 200, 150_000, 100_000,
        "404", 80_000, 30_000, 2000, None]

retention_rate = 0.03

# TODO: run this code
for pop in data:
    time.sleep(0.25)
    try:
        print(f"we retained {retention_rate * pop} users")
    # bug masking
    except TypeError:
        if pop == None:
            # pop = 0
            # print(f"we retained {retention_rate * pop} users")
        else:
            print("Converting string to int")
            pop = int(pop)
            print(f"we retained {retention_rate * pop} users")
            continue
        