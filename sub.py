#!/usr/bin/env python

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.cloud import pubsub_v1

import settings


def show_message(message):
    print(f"Received {message}.")
    # Acknowledge the message. Unack'ed messages will be redelivered.
    message.ack()
    print(f"Acknowledged {message.message_id}.")



def sub(subscription_id, message_handler, timeout=None):
    """Receives messages from a Pub/Sub subscription."""
    # project id
    project_id = settings.PROJECT_ID
    # Initialize a Subscriber client
    subscriber_client = pubsub_v1.SubscriberClient(
        credentials=settings.GOOGLE_APPLICATION_CREDENTIALS
    )
    # Create a fully qualified identifier in the form of
    # `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber_client.subscription_path(project_id, subscription_id)

    def callback(message):
        message_handler(message)

    streaming_pull_future = subscriber_client.subscribe(
        subscription_path, callback=callback
    )
    print(f"Listening for messages on {subscription_path}..\n")

    try:
        # Calling result() on StreamingPullFuture keeps the main thread from
        # exiting while messages get processed in the callbacks.
        streaming_pull_future.result(timeout=timeout)
    except:  # noqa
        streaming_pull_future.cancel()

    subscriber_client.close()
