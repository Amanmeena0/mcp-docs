from fastmcp import FastMCP


mcp = FastMCP(name="Calculator")


@mcp.tool()
def multiply(a: float, b: float)-> float:
    """Multiply two numbers
    args: a(float) first number 
          b(float) second number

    returns: float: the product of the two numbers.
    """
    return a * b


@mcp.tool(
    name = "add",
    description = "Add two numbers",
    tags = ["maths","arthemetic"]
)
def add_numers(x: float,y: float)-> float:
    """
    Add two numbers
    args : x(float) : the first number.
           y(float) : the second number.

    returns : float : the sum of the two numbers.
    """

    return x + y


@mcp.tool()
def subtract(x: float,y: float)-> float:
    """
    subtract two numbers

    args : x(float) : the first number
           y(float) : the second number
    """
    return x - y

@mcp.tool()
def divide(x:float,y: float)-> float:
    """
    divide two numbers

    args : x(float) : the first number
            y(float) : the second number
    """
    return x // y


if __name__ == "__main__":
    mcp.run()