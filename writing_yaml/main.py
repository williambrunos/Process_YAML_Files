import yaml


def main():
    data = {
        'name': 'William',
        'age': 20,
        'address': {
            'city': 'Boston',
            'state': 'Massachusetts',
            'zipcode': '1234'
        }
    }

    # This saves the yaml in the same directory of the main.py
    with open('write.yaml', 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


if __name__ == '__main__':
    main()
