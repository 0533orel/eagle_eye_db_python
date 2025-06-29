"""Command‑line interface entry point for Eagle Eye DB agent management system."""

from dal.agent_dal import DALAgent
from dal.agent_dal import SQLConnection
from validation import get_id, get_name, get_status

def update_menu(dal, id):
    """update_menu function."""
    while True:
        agent = dal.get_agent_by_id(id)

        print("\n--- UPDATE AGENT ---")
        print(agent,"\n")
        print("1. Code name")
        print("2. Name")
        print("3. Location")
        print("4. Status")
        print("5. Increment missions completed")
        print("6. Back to main menu")

        choice = input("\nChoose what to update (1-5): ").strip()


        if choice == '1':
            code_name = input("\nEnter code name: ").strip()
            dal.update_code_name(id, code_name)

        elif choice == '2':
            name = get_name()
            dal.update_name(id, name)

        elif choice == '3':
            location = input("\nEnter location: ").strip()
            dal.update_location(id, location)

        elif choice == '4':
            status = get_status()
            dal.update_status(id, status)

        elif choice == '5':
            dal.update_missions_completed(id)

        elif choice == '6':
            break

        else:
            print("\nInvalid choice. Please select between 1-5.")

def main_menu():
    """main_menu function."""
    conn = SQLConnection("eagleeyedb")
    dal = DALAgent(conn)
    while True:

        print("\n===== EAGLE EYE - AGENT CONTROL MENU =====")
        print("1. View all agents")
        print("2. Add new agent")
        print("3. Update agent")
        print("4. Delete agent")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            agents = dal.get_agents()
            if agents:
                for agent in agents:
                    print(agent)
        elif choice == '2':
            full_name = get_name()
            code_name = input("\nEnter code name: ").strip()
            location  = input("\nEnter location: ").strip()
            dal.add(full_name, code_name, location)

        elif choice == '3':
            agent_id = get_id(dal)
            if agent_id != -1:
                update_menu(dal, agent_id)

        elif choice == '4':
            agent_id = get_id(dal)
            if agent_id != -1:
                dal.delete(agent_id)

        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select between 1-5.")

if __name__ == "__main__":
    main_menu()