import asyncio

async def fake_llm_stream(messages):
    response = "Based on the data, your revenue is 120000 with a growth of 12 percent."
    for token in response.split():
        await asyncio.sleep(0.2)  # simulate streaming delay
        yield token + " "

def fetch_sales_data():
    return {
        "revenue": 120000,
        "growth": "12%"
    }
