from app.config.settings import settings
from app.security.auth import create_access_token
import asyncio
import websockets
import json
import requests
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def test_websocket():
    # Create a mock token
    mock_user = {
        "id": "mock_user_id",
        "email": "hieutt50@example.com",
        "username": "mockuser"
    }
    access_token = create_access_token(
        data={"sub": mock_user["email"]},
        expires_delta=timedelta(minutes=30)
    )

    # Create headers for HTTP requests
    http_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Create a new chat using the API endpoint
    chat_data = {
        "project_id": "672ae44f3443a13286df3aa0"
    }

    try:
        # Create chat using POST /chat endpoint
        response = requests.post(
            "http://localhost:8000/chat/",
            headers=http_headers,
            json=chat_data
        )
        response.raise_for_status()
        chat = response.json()
        chat_id = chat["_id"]

        print(f"\nCreated chat successfully:")
        print(f"Chat ID: {chat_id}")
        print(f"Project ID: {chat['project_id']}")

        # WebSocket connection with token as query parameter
        uri = f"ws://localhost:8000/chat/ws/{chat_id}?token={access_token}"

        print(f"\nConnecting to WebSocket...")
        print(f"Token: {access_token}")

        async with websockets.connect(uri) as websocket:
            print("Connected to WebSocket")
            print("\nYou can now start chatting. Type 'exit' to quit.")

            while True:
                user_input = input("\nYou: ")
                if user_input.lower() == 'exit':
                    break

                message = {
                    "content": user_input,
                    "sender": "user"
                }
                print("\nSending message...")
                await websocket.send(json.dumps(message))

                response = await websocket.recv()
                print(
                    f"\nReceived: {json.dumps(json.loads(response), indent=2)}")

    except requests.exceptions.RequestException as e:
        print(f"HTTP Error: {str(e)}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.text}")
    except websockets.exceptions.WebSocketException as e:
        print(f"WebSocket Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        print(f"Error Type: {type(e)}")

if __name__ == "__main__":
    print("Starting WebSocket test client...")
    asyncio.get_event_loop().run_until_complete(test_websocket())
