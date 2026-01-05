# PSEUDOCODE, Updated & Developed to meet Criteria.

BEGIN PROGRAM
    LOAD inventory data from JSON file
    WHILE user has not chosen to exit DO
        DISPLAY main menu
            1. Add item
            2. View items
            3. Search item
            4. Update item
            5. Delete item
            6. Exit

        GET user menu choice
        IF choice == 1 THEN
            PROMPT user for item ID
            PROMPT user for item name
            PROMPT user for quantity
            PROMPT user for price
            ADD item to inventory list
            SAVE inventory to JSON file
            DISPLAY confirmation message

        ELSE IF choice == 2 THEN
            IF inventory is empty THEN
                DISPLAY "No items available"
            ELSE
                DISPLAY all inventory items
            END IF

        ELSE IF choice == 3 THEN
            PROMPT user for item ID
            SEARCH inventory for matching item
            IF item is found THEN
                DISPLAY item details
            ELSE
                DISPLAY "Item not found"
            END IF

        ELSE IF choice == 4 THEN
            PROMPT user for item ID
            SEARCH inventory for matching item
            IF item is found THEN
                PROMPT user for new quantity
                PROMPT user for new price
                UPDATE item details
                SAVE inventory to JSON file
                DISPLAY confirmation message
            ELSE
                DISPLAY "Item not found"
            END IF

        ELSE IF choice == 5 THEN
            PROMPT user for item ID
            REMOVE item from inventory
            SAVE inventory to JSON file
            DISPLAY confirmation message

        ELSE IF choice == 6 THEN
            DISPLAY "Exiting program"
            EXIT loop

        ELSE
            DISPLAY "Invalid option, please try again"
        END IF
    END WHILE
END PROGRAM
