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


def pub(topic_id, data):
    """Publishes a message to a Pub/Sub topic."""
    # get project id
    project_id = settings.PROJECT_ID
    # Initialize a Publisher client.
    client = pubsub_v1.PublisherClient(
        credentials=settings.GOOGLE_APPLICATION_CREDENTIALS
    )
    # Create a fully qualified identifier of form `projects/{project_id}/topics/{topic_id}`
    topic_path = client.topic_path(project_id, topic_id)

    # When you publish a message, the client returns a future.
    api_future = client.publish(topic_path, data)
    message_id = api_future.result()

    print(f"Published {data} to {topic_path}: {message_id}")

