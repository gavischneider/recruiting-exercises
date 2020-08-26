class InventoryAllocator():
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory

    def ship(self):
        # Make sure we got both inputs
        if not self.order or not self.inventory:
            return []
        else:
            # We got both inputs
            order = self.order
            warehouses = self.inventory

            shipment = {}
            final_shipment = []

            # Iterate over warehouses
            for wh in warehouses:

                # Iterate over every key in order
                for key in order.keys():

                    # Check if the warehouse contains that item
                    if key in wh['inventory'].keys():

                        # Now check if there is enough of that item for this order
                        if wh['inventory'][key] >= order[key]:

                            # We can ship it, add it to the shipment
                            shipment[key] = order[key]

                            # Update stock
                            wh['inventory'][key] -= order[key]

                            # Since we finished with this item, remove it from the order
                            order[key] = 0

                        # If there is not enough of that item in stock
                        else:
                            # We'll take what is in stock
                            shipment[key] = wh['inventory'][key]

                            # Update order
                            order[key] -= wh['inventory'][key]

                            # Update stock
                            wh['inventory'][key] = 0

                # Add item to the final shipment
                final_shipment.append({wh['name']: shipment})

            # When we get here, we've gone through all the warehouses.
            # Now we'll check if we got everything that was in the order
            for key in order.keys():

                # If the number is not 0, we were not able to complete the order
                if order[key] > 0:
                    return []

            # Update self.inventory
            self.inventory = warehouses

            return final_shipment


if __name__ == "__main__":
    ia = InventoryAllocator(
        {'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}])

    print("Shipment Details: ")
    print(ia.ship())
