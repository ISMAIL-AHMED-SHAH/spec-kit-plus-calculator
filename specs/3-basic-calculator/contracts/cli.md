# CLI Contracts: Basic Calculator Operations

This document defines the command-line interface for the calculator library.

## Commands

### `add`

-   **Description**: Adds two numbers.
-   **Usage**: `calculator add <num1> <num2>`
-   **Arguments**:
    -   `num1`: The first number.
    -   `num2`: The second number.
-   **Output**: The sum of the two numbers.

### `subtract`

-   **Description**: Subtracts the second number from the first.
-   **Usage**: `calculator subtract <num1> <num2>`
-   **Arguments**:
    -   `num1`: The first number.
    -   `num2`: The second number.
-   **Output**: The difference of the two numbers.

### `multiply`

-   **Description**: Multiplies two numbers.
-   **Usage**: `calculator multiply <num1> <num2>`
-   **Arguments**:
    -   `num1`: The first number.
    -   `num2`: The second number.
-   **Output**: The product of the two numbers.

### `divide`

-   **Description**: Divides the first number by the second.
-   **Usage**: `calculator divide <num1> <num2>`
-   **Arguments**:
    -   `num1`: The first number.
    -   `num2`: The second number (cannot be zero).
-   **Output**: The quotient of the two numbers.
-   **Error**: If `num2` is zero, an error message will be displayed.
