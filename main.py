import re

# Regular expression pattern to match IP addresses with subnet masks
ip_subnet_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})'

# Function to filter IP addresses with subnet masks in the range of /1 to /32
def filter_and_save_ip_addresses(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
        ip_subnet_matches = re.findall(ip_subnet_pattern, data)

        filtered_ips = [ip for ip in ip_subnet_matches if re.match(r'.*/[1-9]\d*|/32$', ip)]

    with open(output_file, 'w') as out_file:
        out_file.write("IP addresses with subnet masks between /1 and /32:\n")
        for ip in filtered_ips:
            out_file.write(ip + '\n')

if __name__ == "__main__":
    input_file = "raw_table.txt"
    output_file = "filtered_ip_sub.txt"
    filter_and_save_ip_addresses(input_file, output_file)