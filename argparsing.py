import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My description")
    
    # Setting a parameter
    parser.add_argument("--region", default="ap-southeast-1", help="aws region")
    
    # Specifying the type
    parser.add_argument("-p", "--my-param", default=5, type=int, help="Param description")
    
    # Setting options
    parser.add_argument("--model", default="ppo", choices=["ppo", "es", "ars"], help="My learning algorithm")
    
    # Bool Option #1
    parser.add_argument('--gpu', action='store_true')
    
    # Bool Option #2
    parser.add_argument(
        "--mybool",
        dest="mybool",
        action="store_true",
        help="Whether to use this or not",
    )
    parser.add_argument("--no-mybool", dest="mybool", action="store_false")
    parser.set_defaults(mybool=False)
    
    # Parsing the arguments
    args = parser.parse_args()
    print(args)
