def get_id(dal):
    while True:
        try:
            id = int(input("\nEnter agent id: "))
            agent = dal.get_agent_by_id(id)
            if agent:
                return id
            else:
                return -1
        except:
            print("\ninvalid value")


def get_name():
    while True:
        full_name = input("\nEnter full name: ").strip()
        is_valid = True
        for char in full_name:
            if char.isnumeric():
                is_valid = False
                break
        if is_valid:
            return full_name
        else:
            print("\ninvalid value")


def get_status():
    statuses = {
        1: "active",
        2: "injured",
        3: "missing",
        4: "retired"
    }
    while True:
        try:
            status_chose = int(input("\n--- STATUS AGENT ---: \n"
                                     "1. active \n"
                                     "2. injured \n"
                                     "3. missing \n"
                                     "4. retired\n"
                                     "Choose status (1-4): "))
            if 0 < status_chose <= 4:
                return statuses[status_chose]
            else:
                print("\nChose a number between 1-4")
        except:
            print("invalid value... please enter a number between 1-4")

