#nkululeko zwane


que_line = []
def queue_list():
 pass




queue = []

def add_to_queue(customer):
    queue.append(customer)
    print(f"{customer} added to the queue. Position: {len(queue)}")

def serve_next_customer():
    if queue:
        served_customer = queue.pop(0)
        print(f"Customer {served_customer} served.")
        return served_customer
    else:
        print("No customers in the queue.")
        return None

def notify_customer(customer):
    print(f"{customer}, it's your turn!")

# Example usage
if __name__ == "__main__":
    # Adding customers to the queue
    add_to_queue("Alice")
    add_to_queue("Bob")
    add_to_queue("Charlie")

    # Serving customers
    served_customer = serve_next_customer()

    # Notifying the served customer
    if served_customer:
        notify_customer(served_customer)




