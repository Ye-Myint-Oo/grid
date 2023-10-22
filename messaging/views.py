from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QueueMessage
from .serializers import QueueMessageSerializer
from lxml import etree
import threading
import time
from .utils import callback

class QueryRequestView(APIView):
    def post(self, request, queue_name):
        # Extract data from the request
        request_number = request.query_params.get('RequestNumber')
        mail_number = request.query_params.get('MailNumber')
        subject_id = request.query_params.get('SubjectID')
        data_length = request.query_params.get('DataLength')
        aggregate_number = request.query_params.get('AggregateNumber')
        call_back_url = request.query_params.get('call_back_url') #optional (remove later )
        message_xml_data = request.body.decode('utf-8')
        root = etree.fromstring(message_xml_data)
        # Create a dictionary with the data
        data = {
            'queue_name': queue_name,
            'request_number': request_number,
            'mail_number': mail_number,
            'subject_id': subject_id,
            'data_length': data_length,
            'aggregate_number': aggregate_number,
            'message': message_xml_data 
        }

        # Create a serializer instance
        serializer = QueueMessageSerializer(data=data)

        # Check if the data is valid
        if serializer.is_valid():
            # Save the serialized data to the database
            serializer.save()


            def delayed_callback():
                time.sleep(2)
                callback(call_back_url)

            # Create a new thread for the callback function
            callback_thread = threading.Thread(target=delayed_callback)
            callback_thread.start()


            # Return the serialized data in the response
            return Response(serializer.data, status=status.HTTP_201_CREATED,content_type='application/xml')
        else:
            # Return an error response if the data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateMessageView(APIView):    
    def post(self, request, queue_name):
        # Extract data from the request
        request_number = request.query_params.get('RequestNumber')
        mail_number = request.query_params.get('MailNumber')
        subject_id = request.query_params.get('SubjectID')
        data_length = request.query_params.get('DataLength')
        aggregate_number = request.query_params.get('AggregateNumber')
        call_back_url = request.query_params.get('call_back_url')  # Optional (remove later)
        message_xml_data = request.body.decode('utf-8')
        root = etree.fromstring(message_xml_data)

        # Check if the message already exists
        
        queue_messages = QueueMessage.objects.filter(
            queue_name=queue_name,
            request_number=request_number,
            mail_number=mail_number,
            subject_id=subject_id
        )
        if not queue_messages:
            return Response({'message': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update each message
        for queue_message in queue_messages:
            #queue_message.data_length = data_length
            #queue_message.aggregate_number = aggregate_number
            queue_message.message = message_xml_data
            queue_message.save()

        def delayed_callback():
            time.sleep(2)
            callback(call_back_url)

        # Create a new thread for the callback function
        callback_thread = threading.Thread(target=delayed_callback)
        callback_thread.start()

        # Return the serialized data in the response
        serializer = QueueMessageSerializer(queue_message)
        return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/xml')

class BatchDispatchView(APIView):
     def post(self, request, queue_name):
        # Extract data from the request
        request_number = request.query_params.get('RequestNumber')
        mail_number = request.query_params.get('MailNumber')
        subject_id = request.query_params.get('SubjectID')
        data_length = request.query_params.get('DataLength')
        aggregate_number = request.query_params.get('AggregateNumber')
        call_back_url = request.query_params.get('call_back_url') #optional (remove later )
        message_xml_data = request.body.decode('utf-8')
        root = etree.fromstring(message_xml_data)
        # Create a dictionary with the data
        data = {
            'queue_name': queue_name,
            'request_number': request_number,
            'mail_number': mail_number,
            'subject_id': subject_id,
            'data_length': data_length,
            'aggregate_number': aggregate_number,
            'message': message_xml_data 
        }

        # Create a serializer instance
        serializer = QueueMessageSerializer(data=data)

        # Check if the data is valid
        if serializer.is_valid():
            # Save the serialized data to the database
            serializer.save()


            def delayed_callback():
                time.sleep(2)
                callback(call_back_url)

            # Create a new thread for the callback function
            callback_thread = threading.Thread(target=delayed_callback)
            callback_thread.start()


            # Return the serialized data in the response
            return Response(serializer.data, status=status.HTTP_201_CREATED,content_type='application/xml')
        else:
            # Return an error response if the data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
