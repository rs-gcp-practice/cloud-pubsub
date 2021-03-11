import argparse

# from . import settings
import sub


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # parser.add_argument("project_id", help="Google Cloud project ID")
    # parser.add_argument("subscription_id", help="Pub/Sub subscription ID")
    parser.add_argument(
        "timeout", default=None, nargs="?", const=1, help="Pub/Sub subscription ID"
    )

    args = parser.parse_args()
    # if args.project_id is None:
    #     args.project_id = settings.PROJECT_ID
    # if args.subscription_id is None:
    #     args.subscription_id = "greeting-sub-two"

    # sub.sub(args.project_id, args.subscription_id, sub.show_message, args.timeout)
    subscription_id = "greeting-sub-two"
    sub.sub(subscription_id, sub.show_message, args.timeout)
