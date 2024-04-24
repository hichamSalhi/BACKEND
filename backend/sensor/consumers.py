
import django
import os
import json
import asyncio
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from sensor.models import AData, BData, WData, XData, YData, ZData


class DataConsumer(AsyncWebsocketConsumer):

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
            # Fetch the latest data from each model and serialize it into JSON format
            serialized_data = []
            for model_class in [AData, BData, WData, XData, YData, ZData]:
                latest_five_records = await self.get_latest_records(model_class)
                serialized_data.extend([
                    {
                        "id": obj.id,
                        "SensorID": obj.SensorID,
                        "Date_n_Time": obj.Date_n_Time,  # Format the datetime as needed
                        "Value": getattr(obj, model_class.__name__[0])  # Get the value field dynamically
                    }
                    for obj in latest_five_records
                ])

            # Send the serialized data to the client
            await self.send(text_data=json.dumps(serialized_data))

            # Adjust the sleep time to one hour
            await asyncio.sleep(1)

    @database_sync_to_async
    def get_latest_records(self, model_class):
        # Retrieve the latest five records from the specified model
        latest_five_records = model_class.objects.using('iot').order_by('-Date_n_Time')[:5]
        print("Latest five records for", model_class.__name__, ":", latest_five_records)

        return list(latest_five_records)