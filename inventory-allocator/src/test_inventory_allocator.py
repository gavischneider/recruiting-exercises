import unittest

from inventory_allocator import InventoryAllocator


class Test(unittest.TestCase):

    # All good
    def test_one(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.ship(), output)

    # All good
    def test_two(self):
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {
            'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.ship(), output)

    # Not enough stock
    def test_three(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.ship(), output)

    # Not enough stock
    def test_four(self):
        order = {'apple': 2}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.ship(), output)

    # Missing parameter
    def test_five(self):
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.ship(), output)

    # Missing parameter
    def test_six(self):
        order = {'apple': 2}
        inventory = []
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.ship(), output)


if __name__ == "__main__":
    unittest.main()
