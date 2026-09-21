"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart.keys():
            current_cart[item] += 1
            
        else:
            current_cart.setdefault(item, 1)
    return current_cart
            
    


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    notes_dict = {}
    for item in notes:
        if item in notes_dict.keys():
            notes_dict[item] += 1

        else:
            notes_dict.setdefault(item, 1)
    return notes_dict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    new_ideas = ideas.copy()
    for new_recipe, new_ingredients in recipe_updates:
        new_ideas[new_recipe] = new_ingredients

    return new_ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_dict = {}
    sorted_cart = sorted(cart.keys(), reverse = True)

    for key in sorted_cart:
        quantity = cart[key]
        aisle, fridge = aisle_mapping[key]
        fulfillment_dict[key] = [quantity, aisle, fridge]

    return fulfillment_dict

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    updated_inventory = {}
    for key in store_inventory:
        inventory, aisle, fridge = store_inventory[key]
        if key in fulfillment_cart.keys():
            need, aisle, fridge = fulfillment_cart[key]
            quantity = inventory - need
            if quantity <= 0:
                quantity = 'Out of Stock'
        else:
            quantity = inventory
        
        updated_inventory[key] = [quantity, aisle, fridge]
    return updated_inventory
        
        
