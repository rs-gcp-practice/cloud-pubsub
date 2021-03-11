import argparse

# from . import settings
import pub


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # parser.add_argument("project_id", help="Google Cloud project ID")
    # parser.add_argument("topic_id", help="Pub/Sub topic ID")

    args = parser.parse_args()

    # Data sent to Cloud Pub/Sub must be a bytestring.
    data = b"Hello, World!"

    # if args.project_id is None:
    #     args.project_id = settings.PROJECT_ID
    # if args.topic_id is None:
    #     args.topic_id = "greeting-topic"

    # pub.pub(args.project_id, args.topic_id, data)
    topic_id = "greeting-topic"
    pub.pub(topic_id, data)
