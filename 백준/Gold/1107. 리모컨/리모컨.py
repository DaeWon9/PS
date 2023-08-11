import sys

def get_available_adjoin_number(target_number):
    minus_number = target_number
    plus_number = target_number
    result_list = ["", ""]
    while True:
        minus_number -= 1
        plus_number += 1
        if minus_number < 0 and plus_number > 9:
            break

        if str(minus_number) in available_key:
            result_list[0] = str(minus_number)

        if str(plus_number) in available_key:
            result_list[1] = str(plus_number)

        if result_list[0] != "" or result_list[1] != "":
            break

    return result_list

remocon_key = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
default_channel = 100

target_channel = str(sys.stdin.readline())
target_channel_length = len(target_channel) - 1

break_down_count = int(sys.stdin.readline())
break_down_key = []
if break_down_count > 0:
    break_down_key = list(map(str, sys.stdin.readline().split()))

available_key = [key for key in remocon_key if key not in break_down_key]

try_channel_list = []

press_count = abs(int(target_channel) - default_channel)
flag = False

if len(available_key) > 0:
    try_channel_list.append(max(available_key) * (target_channel_length - 1))
    try_channel_list.append(min(available_key) * (target_channel_length + 1))
    try_channel_list.append(min(available_key) * target_channel_length)

if "1" in available_key:
    try_channel_list.append("1" + min(available_key) * target_channel_length)

for key in available_key:
    try_channel_list.append(key + max(available_key) * (target_channel_length - 1))
    try_channel_list.append(key + min(available_key) * (target_channel_length - 1))

for index in range(target_channel_length):
    min_number, max_number = get_available_adjoin_number(int(target_channel[index]))

    if len(available_key) > 0 and index > 0:
        try_channel_list.append(
            target_channel[0:index]
            + min_number
            + max(available_key) * (target_channel_length - index - 1)
        )
        try_channel_list.append(
            target_channel[0:index]
            + max_number
            + min(available_key) * (target_channel_length - index - 1)
        )

    if len(available_key) > 0 and target_channel[index] not in available_key:
        flag = True
        try_channel_list.append(
            target_channel[0:index]
            + min_number
            + max(available_key) * (target_channel_length - index - 1)
        )
        try_channel_list.append(
            target_channel[0:index]
            + max_number
            + min(available_key) * (target_channel_length - index - 1)
        )
        try_channel_list.append(
            min_number + min(available_key) * (target_channel_length)
        )
        break

if len(available_key) > 0 and flag == False:
    press_count = min(target_channel_length, press_count)

for channel in set(try_channel_list):
    if len(channel) > 0:
        channel_len = len(channel)
        if int(channel) == 0:
            channel_len = 1
        press_count = min(
            abs(int(target_channel) - int(channel)) + channel_len, press_count
        )

print(press_count)