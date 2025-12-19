from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- IMPORT THIS
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Calculator APP")

# --- ADD THIS BLOCK ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows connections from the Inspector
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """
    Multiply two numbers.
    """
    result = a * b
    return {"result": result}

@app.post("/add")
def add_numbers(a: float, b: float):
    """
    Add two numbers.
    """
    result = a + b
    return {"result": result}

@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    """
    Subtract b from a.
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
def divide_numbers(a: float, b: float):
    """
    Divide a by b.
    """
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    result = a / b  # Changed // to / for float division, otherwise 5.0 // 2.0 = 2.0
    return {"result": result}


# convert it to mcp
mcp = FastApiMCP(app, name="calculatorMcp")
# By default, this mounts at /sse and /messages
mcp.mount_http() 

if __name__ == "__main__":
    import uvicorn
    # Use 127.0.0.1 instead of localhost to avoid some Windows ipv6 issues
    uvicorn.run(app, host="127.0.0.1", port=8002)