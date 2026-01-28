# Exercise — IPv4 Address Ranking
# Problem Statement
# You are given a list of IPv4 addresses represented as strings.
# Your task is to:
# Convert each IPv4 address into its 32-bit integer representation.
# Sort the addresses from the smallest to the largest value.
# Assign a ranking level to each address:
# The smallest address receives level 1
# The second smallest receives level 2
# And so on
# If two or more addresses are equal, they must receive the same level (dense ranking).
# Return an array containing the ranking level of each IPv4 address in the original input order.
def ranking_adresses(adresses):
    def convert_to_int(adress):
        parts = adress.split(".")
        sum = (
            int(parts[0]) * 256 **3 +
            int(parts[1]) * 256 **2 +
            int(parts[2]) * 256 +
            int(parts[3]) * 1 
        )
        return sum
    converted = [convert_to_int(adress) for adress in adresses]
    filtered = sorted(set(converted))
    ranking = { value : i + 1  for i, value in enumerate(filtered)}
    return [ranking[value] for value in converted]

def tests(ips, expected):
    success, error = 0 , 0 
    if ranking_adresses(ips) == expected:
        success += 1
    else:
        error +=1
    print( f"Passed tests: {success} \nFailed tests:{error}")
 
ips = [
    "172.16.0.1",
    "10.0.0.1",
    "192.168.0.1"
]
expected = [2, 1, 3]
tests(ips, expected)