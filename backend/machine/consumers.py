
import django
import os
import json
import asyncio


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from machine.models import Machine1, Machine2, Machine3, Machine4


class MachineConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Accept communication
        await self.accept()
        # Start publishing data when the client connects
        await self.publish_data()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def publish_data(self):
        while True:
            # Query all objects from each model using sync_to_async
            machine_1_data = await sync_to_async(list)(Machine1.objects.all().values())
            machine_2_data = await sync_to_async(list)(Machine2.objects.all().values())
            machine_3_data = await sync_to_async(list)(Machine3.objects.all().values())
            machine_4_data = await sync_to_async(list)(Machine4.objects.all().values())

            # Serialize the data into JSON format
            serialized_data = {
                'machine_1': machine_1_data,
                'machine_2': machine_2_data,
                'machine_3': machine_3_data,
                'machine_4': machine_4_data
            }
            # Send the serialized data to the client
            await self.send(text_data=json.dumps(serialized_data))

            # Adjust the sleep time to one hour
            await asyncio.sleep(1)